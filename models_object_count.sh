#!/bin/bash

MANAGE=django-admin.py

FILENAME='logs/'`date +"%d.%m.%Y"`'.dat'
mkdir -p logs
PYTHONPATH=`pwd`'/cctest' DJANGO_SETTINGS_MODULE=cctest.settings $MANAGE models_info 2>$FILENAME
