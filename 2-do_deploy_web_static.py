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
