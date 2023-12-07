#!/usr/bin/python3
"""a Fabric script (based on the file 2-do_deploy_web_static.py)
that creates and distributes an archive to your web servers,
using the function deploy"""
from os import path
from fabric.operations import run, put, local
from fabric.api import env, execute
from datetime import datetime

env.hosts = ["54.90.6.47", "100.25.34.49"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/school"


def do_pack():
    """function to archieve the web_static contents"""
    try:
        if not path.exists("versions"):
            local("mkdir -p versions")
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_filename = "versions/web_static_{}.tgz".format(timestamp)
        command = "tar -cvzf {} web_static".format(archive_filename)
        result = local(command, capture=True)
        if result.failed:
            return None
        print(result)
        file_size = path.getsize("{}".format(archive_filename))
        print(
            "web_static packed: \
{} -> {}Bytes".format(
                archive_filename, file_size
            )
        )
        return archive_filename
    except BaseException:
        return None


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
        print("New version deployed!")
        return True
    except BaseException:
        return False


def deploy():
    """function that creates and distributes an archive to your web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    deployed = do_deploy(archive_path)
    return deployed
