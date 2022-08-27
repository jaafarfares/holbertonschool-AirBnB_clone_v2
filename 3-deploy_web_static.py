#!/usr/bin/python3
"""
Write a Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers, using the function do_deploy:
"""
from fabric.api import put, run, env
from fabric.api import local
from datetime import datetime
from os.path import isdir, exists
env.hosts = ['34.224.57.138', '54.209.132.114']


def do_pack():
    """
    the function do_pack that returns archive path that been generated
    """
    if isdir("versions") is False:
        local("mkdir versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    namee = "versions/web_static_{}.tgz".format(date)
    local("tar -cvzf {} web_static".format(namee))
    if exists(namee):
        return namee
    return None


def do_deploy(archive_path):
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


def deploy():
    """distributes the archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
