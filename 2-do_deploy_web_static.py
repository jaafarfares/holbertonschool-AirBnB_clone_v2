#!/usr/bin/python3
"""
Write a Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers, using the function do_deploy:
"""
from fabric.api import put, run, env
from os.path import exists
env.hosts = ['34.224.57.138', '54.209.132.114']


def do_deploy(archive_path):
    """ this is a usles comment """
    if exists(archive_path):
        s = archive_path.split("/")[-1]
        se = s.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, se))
        run('tar -xzf /tmp/{} -C {}{}/'.format(s, path, se))
        run('rm /tmp/{}'.format(s))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, se))
        run('rm -rf {}{}/web_static'.format(path, se))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, se))
        return True

    return False
