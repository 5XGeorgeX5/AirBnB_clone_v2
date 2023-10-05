#!/usr/bin/python3
"""
creates and distributes an archive to your web servers,
using the function deploy.
"""
from fabric.api import local, run, put, env
from os.path import isfile
from datetime import datetime


env.hosts = ['100.26.166.229', '34.202.157.96']
env.user = 'ubuntu'


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

def do_deploy(archive_path):
    """distributes an archive to your web servers"""
    if not isfile(archive_path):
        return False
    try:
        archive = archive_path.split('/')[-1]
        path = "/data/web_static/releases/{}".format(archive.split('.')[0])
        tmp = "/tmp/{}".format(archive)
        put(archive_path, '/tmp/')
        run("rm -rf {}/".format(path))
        run("mkdir -p {}".format(path))
        run("tar -xzf {} -C {}/".format(tmp, path))
        run("rm {}".format(tmp))
        run("mv {}/web_static/* {}/".format(path, path))
        run("rm -rf {}/web_static".format(path))
        run("rm -rf /data/web_static/current")
        run("ln -s {}/ /data/web_static/current".format(path))
        return True
    except Exception:
        return False

def deploy():
    """creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
