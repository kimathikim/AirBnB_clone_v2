#!/usr/bin/env bash
# first script to set up web servers for deployment of web_static
# install nginx
# create folders
# create fake html file
# create symbolic link
# change ownership of symbolic link
# change ownership of folder
# update nginx config file
# restart nginx
sudo apt-get update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "Conquistando desde dentro" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '42i \\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default
sudo service nginx restart
