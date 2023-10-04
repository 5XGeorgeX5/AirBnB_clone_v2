#!/usr/bin/python3
"""
generates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo, using the function do_pack.
"""
from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """generates a .tgz archive from the contents of the web_static folder"""
    local("sudo mkdir -p versions")
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = "versions/web_static_{}.tgz".format(time)
    command = local("sudo tar -cvzf {} web_static".format(file_path))
    if command.succeeded:
        return file_path
    else:
        return None
