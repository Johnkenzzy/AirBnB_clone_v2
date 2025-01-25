#!/usr/bin/env bash
# Script that sets up your web servers for the deployment of web_static.

# Install Nginx if not already installed
if ! dpkg -l | grep -q nginx; then
  sudo apt update
  sudo apt install -y nginx
fi

# Create necessary directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file for testing
echo "<html>
  <head>
  </head>
  <body>
    ALX - Deployment Test
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create (or recreate) symbolic link
if [ -L /data/web_static/current ]; then
  sudo rm /data/web_static/current
fi
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve /data/web_static/current/ at /hbnb_static
nginx_conf="/etc/nginx/sites-available/default"
sudo sed -i '/location \/hbnb_static {/,/}/d' $nginx_conf
sudo sed -i '/server_name _;/a \\n    location /hbnb_static {\n        alias /data/web_static/current/;\n        index index.html;\n    }' $nginx_conf

# Restart Nginx to apply changes
sudo service nginx restart

exit 0
