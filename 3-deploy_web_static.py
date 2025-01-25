from fabric.api import env, local, put, run
from datetime import datetime
import os

# Define the web servers' IPs
env.hosts = ['ubuntu@54.144.249.38', 'ubuntu@54.90.63.175']


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.

    Returns:
        str: The path to the created archive if successful, None otherwise.
    """
    try:
        # Create the versions folder if it doesn't exist
        local("mkdir -p versions")

        # Generate the archive filename with the current timestamp
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = f"versions/web_static_{timestamp}.tgz"

        # Create the archive
        result = local(f"tar -czvf {archive_path} web_static")
        if result.failed:
            return None

        return archive_path
    except Exception as e:
        print(f"Error during packing: {e}")
        return None


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
        run(f"mkdir -p {release_folder}")
        run(f"tar -xzf {remote_path} -C {release_folder}")
        run(f"rm {remote_path}")

        # Move the uncompressed content to the proper directory
        run(f"mv {release_folder}/web_static/* {release_folder}/")
        run(f"rm -rf {release_folder}/web_static")

        # Delete the old symbolic link and create a new one
        run("rm -rf /data/web_static/current")
        run(f"ln -s {release_folder} /data/web_static/current")

        return True

    except Exception as e:
        print(f"Error during deployment: {e}")
        return False


def deploy():
    """
    Creates and distributes an archive to the web servers.

    Returns:
        bool: True if all operations were successful, otherwise False.
    """
    archive_path = do_pack()
    if not archive_path:
        return False

    return do_deploy(archive_path)
