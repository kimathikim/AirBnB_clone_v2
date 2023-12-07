#!/usr/bin/python3
"""  a Fabric script (based on the file 1-pack_web_static.py) that
distributes an archive to your web servers, using the function do_deploy"""
from os import path
from fabric.operations import run, put
from fabric.api import env

env.hosts = ["54.90.6.47", "100.25.34.49"]
env.user = "ubuntu"


def do_deploy(archive_path):
    """function that distributes an archive to your web servers"""
    if not path.exists(archive_path):
        return False
    try:
        # send the files th /tmp/ in the server
        put(archive_path, "/tmp/")
        # detach /tmp/ form the file name
        file_name = archive_path.split("/")[-1]
        # detach .tgz from the file name
        file_name1 = file_name.split(".")[0]
        # create the path where the file will be decompressed
        path_file = "/data/web_static/releases/{}".format(file_name1)
        run("mkdir -p {}".format(path_file))
        # decompress the file in the path_file
        run("tar -xzf /tmp/{} -C {}".format(file_name, path_file))
        # delete the archive from the web server
        run("rm /tmp/{}".format(file_name))
        # move the files to the path_file
        run("mv {}/web_static/* {}/".format(path_file, path_file))
        # delete the folder web_static
        run("rm -rf {}/web_static".format(path_file))
        # delete the symbolic link /data/web_static/current from the web server
        run("rm -rf /data/web_static/current")
        # create a new symbolic link
        run("ln -s {} /data/web_static/current".format(path_file))
        run('echo "New version deployed!"')
        return True
    except BaseException:
        return False
