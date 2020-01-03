#!/usr/bin/env bash
#Setting webservers
if [ ! -x /usr/sbin/nginx ]; then
    apt-get update
    apt-get -y install nginx
fi

if [ ! -d data/ ]; then
    mkdir data
fi

if [ ! -d data/web_static/ ]; then
    mkdir data/web_static/
fi

if [ ! -d data/web_static/releases/ ]; then
    mkdir data/web_static/releases/
fi

if [ ! -d data/web_static/shared/ ]; then
    mkdir data/web_static/shared/
fi

if [ ! -d data/web_static/releases/test/ ]; then
    mkdir data/web_static/releases/test/
fi

touch data/web_static/releases/test/index.html

echo "This is a test" > data/web_static/releases/test/index.html

if [ -h data/web_static/current ]; then
    rm data/web_static/current
fi

ln -s data/web_static/releases/test/ data/web_static/current
chown -R ubuntu:ubuntu data
root="root \/var\/www\/html;"
alias="alias \/data\/web_static\/current\/hbnb_static;"
sed -i "s/$root/$alias/g" /etc/nginx/sites-enabled/default
sudo service nginx restart
