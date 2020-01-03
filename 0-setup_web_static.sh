#!/usr/bin/env bash
#Setting webservers
if [ ! -x /usr/sbin/nginx ]; then
    apt-get update
    apt-get -y install nginx
fi

if [ ! -d /data ]; then
    mkdir /data
fi

if [ ! -d /data/web_static/ ]; then
    mkdir /data/web_static/
fi

if [ ! -d /data/web_static/releases/ ]; then
    mkdir /data/web_static/releases/
fi

if [ ! -d /data/web_static/shared/ ]; then
    mkdir /data/web_static/shared/
fi

if [ ! -d /data/web_static/releases/test/ ]; then
    mkdir /data/web_static/releases/test/
fi

touch /data/web_static/releases/test/index.html

echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

if [ -h /data/web_static/current ]; then
    rm /data/web_static/current
fi

ln -s /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data
location="location \/hbnb_static {\n\talias \/data\/web_static\/current\/;\n\t}"
sed -i "/listen [::]:80 default_server;/a $location" /etc/nginx/sites-enabled/default
sudo service nginx restart
