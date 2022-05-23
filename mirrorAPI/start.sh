#!/bin/sh
sleep 5
cd /mirror/mirrorAPI
nohup python manage.py runserver 0.0.0.0:8000 &