MANAGE=django-admin.py

test:
	PYTHONPATH=`pwd`'/cctest' DJANGO_SETTINGS_MODULE=cctest.settings $(MANAGE) test main

run:
	PYTHONPATH=`pwd`'/cctest' DJANGO_SETTINGS_MODULE=cctest.settings $(MANAGE) runserver

syncdb:
	PYTHONPATH=`pwd`'/cctest' DJANGO_SETTINGS_MODULE=cctest.settings $(MANAGE) syncdb --noinput