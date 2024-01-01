#!/usr/bin/python3
"""  a Fabric script (based on the file 1-pack_web_static.py) that
distributes an archive to your web servers, using the function do_deploy"""
from os import path
from fabric.operations import run, put
from fabric.api import env

env.hosts = ["18.204.10.133"]
env.user = "ubuntu"


def do_deploy(archive_path):
    """function that distributes an archive to your web servers"""
    if not path.exists(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        file_name = archive_path.split("/")[-1]
        file_name1 = file_name.split(".")[0]
        path_file = "/data/web_static/releases/{}".format(file_name1)
        run("mkdir -p {}".format(path_file))
        run("tar -xzf /tmp/{} -C {}".format(file_name, path_file))
        run("rm /tmp/{}".format(file_name))
        run("mv {}/web_static/* {}/".format(path_file, path_file))
        run("rm -rf {}/web_static".format(path_file))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(path_file))
        print("New version deployed!")
        return True
    except BaseException:
        return False
