#!/usr/bin/python3
"""
distributes an archive to your web servers, using the function do_deploy.
"""
from fabric.api import run, put, local, env
from datetime import datetime
from os.path import exists


env.hosts = ['100.26.166.229', '34.202.157.96']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """distributes an archive to your web servers"""
    if not exists(archive_path):
        return False
    archive = archive_path.split('/')[-1]
    path = "/data/web_static/releases/{}".format(archive.split('.')[0])
    tmp = "/tmp/{}".format(archive)
    try:
        put(archive_path, '/tmp/')
        run("mkdir -p {}".format(path))
        run("tar -xzf {} -C {}".format(tmp, path))
        run("rm {}".format(tmp))
        run("mv {}/web_static/* {}/".format(path, path))
        run("rm -rf {}/web_static".format(path))
        run("rm -rf /data/web_static/current")
        run("ln -sf {}/ /data/web_static/current".format(path))
        return True
    except:
        return False
