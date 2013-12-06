MANAGE=django-admin.py

test:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=cctest.settings $(MANAGE) test main

run:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=cctest.settings $(MANAGE) runserver

syncdb:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=cctest.settings $(MANAGE) syncdb --noinput
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=cctest.settings $(MANAGE) migrate --no-initial-data
	
