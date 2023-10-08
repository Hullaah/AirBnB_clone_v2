#!/usr/bin/python3
"""deploys the airbnb webstatic"""
from fabric.api import local
from datetime import datetime
from os import path
from fabric.api import put, run, env


env.hosts = ["54.160.84.211", "54.172.244.75"]


def do_pack():
    """generates a .tgz archive from the contents of the web_static
    folder of your AirBnB Clone"""
    now = str(datetime.now())
    now = now[:now.find('.')]
    date = "".join([x for x in now if x.isdigit()])
    try:
        local("mkdir -p versions")
        print("Packing web_static to versions/web_static_{}.tgz".format(date))
        local("tar -cvzf versions/web_static_{}.tgz web_static".format(date))
        return "versions/web_static_{}.tgz".format(date)
    except Exception:
        return


def do_deploy(archive_path):
    """distributes an archive to your web servers"""
    if not path.exists(archive_path):
        return False
    archive_file = "/tmp/" + archive_path[9:]
    latest_release = "/data/web_static/releases/" + archive_path[9:-4]
    put(archive_path, "/tmp/")
    run("sudo mkdir -p {}".format(latest_release))
    run("sudo tar -xzf {} -C {}".format(archive_file, latest_release))
    run("sudo rm {}".format(archive_file))
    run("sudo mv {location}/web_static/* {location}".format(
        location=latest_release))
    run("sudo rm -rf {}/web_static".format(latest_release))
    run("sudo rm -rf /data/web_static/current")
    run("sudo ln -s {} /data/web_static/current".format(latest_release))
    print("New version deployed!")
    return True


def deploy():
    """deploys the airbnb web static"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
