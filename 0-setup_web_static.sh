#!/usr/bin/env bash
# Prepare your web servers

sudo apt-get update -y
sudo apt-get install nginx -y
mkdir -p  /data/web_static/ && mkdir -p /data/web_static/releases/test/ && mkdir /data/web_static/shared/
echo "from the ashes i will rise" | sudo tee /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown ubuntu:ubuntu -hR /data/
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx restart
