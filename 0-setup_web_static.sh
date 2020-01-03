#!/usr/bin/env bash
#Setting webservers
apt-get -y update
apt-get -y install nginx
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html

echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
location="location \/hbnb_static\/ {\n\talias \/data\/web_static\/current\/;\n\t}"
sed -i "19i $location" /etc/nginx/sites-enabled/default
service nginx restart
