#!/usr/bin/python3
"""
deletes out-of-date archives, using the function do_clean.
"""
from fabric.api import local, run, env


env.hosts = ['100.26.166.229', '34.202.157.96']
env.user = 'ubuntu'


def do_clean(number=0):
    """deletes out-of-date archives"""
    number = int(number)
    if number == 0:
        number = 2
    else:
        number += 1

    local("cd versions; ls -t | tail -n +{} | xargs rm -rf".format(number))
    path = "/data/web_static/releases"
    run("cd {}; ls -t | tail -n +{} | xargs rm -rf".format(path, number))
