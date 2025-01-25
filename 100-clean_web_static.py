#!/usr/bin/python3
"""
Deletes out-of-date archives, using the function do_clean.
"""
from fabric.api import *
import os

# Define the hosts to perform operations on
env.hosts = ['ubuntu@54.144.249.38', 'ubuntu@54.90.63.175']


def do_clean(number=0):
    """
    Deletes out-of-date archives.

    Args:
        number (int): Number of archives to keep. Defaults to 0.
                      - If 0 or 1, keep only the most recent archive.
                      - If 2, keep the two most recent archives, etc.
    """
    number = int(number)

    # Ensure at least one archive is kept
    if number == 0:
        number = 1

    # Clean local archives
    local_archives = sorted(os.listdir("versions"))
    archives_to_delete = local_archives[:-number]
    for archive in archives_to_delete:
        local(f"rm -f versions/{archive}")

    # Clean remote archives
    with cd("/data/web_static/releases"):
        remote_archives = run("ls -tr").split()
        remote_archives = [a for a in remote_archives if "web_static_" in a]
        archives_to_delete = remote_archives[:-number]
        for archive in archives_to_delete:
            sudo(f"rm -rf /data/web_static/releases/{archive}")
