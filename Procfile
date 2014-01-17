web: gunicorn myproject.wsgi.prod
web: python manage.py collectstatic --settings=myproject.settings.prod
web: python manage.py schemamigration --auto --settings=myproject.settings.prod
web: python manage.py syncdb --settings=myproject.settings.prod
