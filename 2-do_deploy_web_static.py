#!/usr/bin/python3
"""distributes an archive to your web servers"""
from os import path
from fabric.api import put, run, env
env.hosts = ["54.160.84.211", "54.172.244.75"]


def do_deploy(archive_path):
    """distributes an archive to your web servers"""
    if not path.exists(archive_path):
        return False
    archive_file = archive_path[9:]
    put(archive_path, "/tmp/")
    run("sudo mkdir -p /data/web_static/releases/{}/".format(
        archive_file[:-4]))
    run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
        archive_file,
        archive_file[:-4]))
    run("sudo rm -rf /tmp/{}".format(archive_file))
    run("sudo mv /data/web_static/releases/" + archive_file[:-4] + "/web_static/*" +
        " /data/web_static/releases/{}".format(archive_file[:-4]))
    run("sudo rm -rf /data/web_static/releases/{}/web_static/".format(
        archive_file[:-4]))
    run("sudo rm -rf /data/web_static/current")
    run("sudo ln -s /data/web_static/releases/{}/ /data/web_static/current"
        .format(archive_file[:-4]))
    print("New version deployed!")
    return True
