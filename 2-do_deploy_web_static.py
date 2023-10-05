#!/usr/bin/python3
"""
distributes an archive to your web servers, using the function do_deploy.
"""
from fabric.api import run, put, env
from os.path import isfile


env.hosts = ['100.26.166.229', '34.202.157.96']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """distributes an archive to your web servers"""
    if not isfile(archive_path):
        return False
    try:
        archive = archive_path.split('/')[-1]
        path = "/data/web_static/releases/{}".format(archive.split('.')[0])
        tmp = "/tmp/{}".format(archive)
        put(archive_path, '/tmp/')
        run("sudo mkdir -p {}".format(path))
        run("sudo tar -xzf {} -C {}/".format(tmp, path))
        run("sudo rm {}".format(tmp))
        run("suod mv {}/web_static/* {}/".format(path, path))
        run("sudo rm -rf {}/web_static".format(path))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {}/ /data/web_static/current".format(path))
        return True
    except Exception:
        return False
