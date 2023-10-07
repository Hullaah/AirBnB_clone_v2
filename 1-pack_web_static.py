#!/usr/bin/python3
"""generates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """generates a .tgz archive from the contents of the web_static
    folder of your AirBnB Clone"""
    now = str(datetime.now())
    now = now[:now.find('.')]
    date = "".join([x for x in now if x.isdigit()])
    local("mkdir -p versions")
    print("Packing web_static to versions/web_static_{}.tgz".format(date))
    local("tar -cvzf versions/web_static_{}.tgz web_static".format(date))
