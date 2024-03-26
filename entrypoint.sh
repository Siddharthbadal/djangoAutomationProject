#!/bin/ash

echo "Applydatabase migration"
python manage.py migrate 

exec "$@"