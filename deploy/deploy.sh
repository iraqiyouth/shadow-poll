#!/bin/sh

kill -9 $(cat /tmp/shadowpoll.pid)
python /var/lib/buildbot/slave/shadow-poll/build/manage.py syncdb --noinput
rm -rf /var/www/shadowpoll/*
cp -r /var/lib/buildbot/slave/shadow-poll/build/* /var/www/shadowpoll
python /var/www/shadowpoll/manage.py runfcgi -v 2 host=127.0.0.1 port=8801 debug=1 pidfile=/tmp/shadowpoll.pid outlog=/var/log/shadowpoll/fcgi.log errlog=/var/log/shadowpoll/fcgi-error.log