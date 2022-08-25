#!/usr/bin/python3
"""Write a
Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack.
"""

from fabric.api import local
from datetime import datetime
from os.path import isdir ,exists


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
