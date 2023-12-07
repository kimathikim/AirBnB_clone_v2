#!/usr/bin/python3
"""Write a Fabric script that generates a .tgz archive
from the contents of the web_static folder of your AirBnB Clone repo,
using the function do_pack"""
import os
from fabric.operations import local
from datetime import datetime


def do_pack():
    """creates a versions dir if not already exist"""
    local("mkdir -p versions")
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "versions/web_static_{}.tgz".format(timestamp)
    command = "tar -cvzf {} web_static".format(archive_name)
    result = local(command, capture=True)
    if result.failed:
        return None

    file_size = os.path.getsize("{}".format(archive_name))
    print(result)
    print("web_static packed: {} -> {}Bytes".format(archive_name, file_size))
    return result
