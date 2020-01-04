#!/usr/bin/python3
""" Module """
from fabric.api import run, local, put
from datetime import datetime


def do_pack():
    """ Funciton """
    local("mkdir -p versions")
    date = datetime.now()
    date = date.strftime("%Y%m%d%H%M%S")
    result = local("tar -cvzf versions/web_static_{}.tgz web_static".
                   format(date))

    if result.failed:
        return None
    return "versions/web_static_{}.tgz web_static".format(date)
