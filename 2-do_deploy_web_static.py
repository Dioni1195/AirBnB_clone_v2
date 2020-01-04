#!/usr/bin/python3
""" Module """
from fabric.api import run, local, put, env
from datetime import datetime
from os import path


env.hosts = ['35.185.25.151', '34.73.128.159']


def do_pack():
    """ Function compress the files """
    local("mkdir -p versions")
    date = datetime.now()
    date = date.strftime("%Y%m%d%H%M%S")
    result = local("tar -cvzf versions/web_static_{}.tgz web_static".
                   format(date))

    if result.failed:
        return None
    return "versions/web_static_{}.tgz web_static".format(date)


def do_deploy(archive_path):
    """ Function to deploy files to servers """
    result_list = []
    if not path.exists(archive_path):
        return False
    name = archive_path.split("/")
    file_name = name[1]
    file_dir = name[1][:-4]
    put(archive_path, "/tmp/{}".format(file_name))
    result_list.append(run("mkdir -p /data/web_static/releases/{}/".
                       format(file_name)))
    result_list.append(run("tar -xzf {} /data/web_static/releases/{}/".
                       format(file_name, file_dir)))
    result_list.append(run("rm /tmp/{}".
                       format(file_name)))
    result_list.append(run("mv /data/web_static/releases/{}/web_static/*\
                            /data/web_static/releases/{}/".format(
                                    file_dir, file_dir)))
    result_list.append(run("rm -rf /data/web_static/releases/{}/web_static".
                       format(file_dir)))
    result_list.append(run("rm -rf /data/web_static/current"))
    result_list.append(run("ln -s /data/web_static/releases/{}/\
                            /data/web_static/current".format(file_dir)))
    for result in result_list:
        if result.failed:
            return False
    print("New version deployed!")
    return True
