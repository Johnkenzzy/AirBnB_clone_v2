#!/usr/bin/python3
"""
Fabric script defining the function do_deploy
"""
from fabric.api import env, put, run, sudo
import os

# Define the web servers' IPs
env.hosts = ['ubuntu@54.144.249.38', 'ubuntu@54.90.63.175']


def do_deploy(archive_path):
    """
    Distributes an archive to web servers.

    Args:
        archive_path (str): Path to the archive file.

    Returns:
        bool: True if all operations were successful, otherwise False.
    """
    if not os.path.exists(archive_path):
        return False

    try:
        # Extract archive filename and folder name
        archive_file = os.path.basename(archive_path)
        archive_name = archive_file.split('.')[0]
        remote_path = f"/tmp/{archive_file}"
        release_folder = f"/data/web_static/releases/{archive_name}"

        # Upload the archive to the /tmp/ directory on the server
        put(archive_path, remote_path)

        # Uncompress the archive to the release folder
        sudo(f"mkdir -p {release_folder}")
        sudo(f"tar -xzf {remote_path} -C {release_folder}")
        sudo(f"rm {remote_path}")

        # Move the uncompressed content to the proper directory
        sudo(f"mv {release_folder}/web_static/* {release_folder}/")
        sudo(f"rm -rf {release_folder}/web_static")

        # Delete the old symbolic link and create a new one
        sudo("rm -rf /data/web_static/current")
        sudo(f"ln -s {release_folder} /data/web_static/current")

        return True

    except Exception as e:
        print(f"An error occurred: {e}")
        return False
