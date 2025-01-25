#!/usr/bin/python3
"""
Fabric script defining the function do_pack
"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    Returns:
        str: The archive path if successful, otherwise None.
    """
    # Create the versions folder if it doesn't exist
    archive_dir = "versions"
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)

    # Generate the archive name with a timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = f"{archive_dir}/web_static_{timestamp}.tgz"

    # Create the .tgz archive using the tar command
    try:
        local(f"tar -czvf {archive_path} web_static")
        return archive_path
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
