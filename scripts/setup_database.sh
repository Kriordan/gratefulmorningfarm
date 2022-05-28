#!/bin/bash

#TODO: This doesn't handle test databases correctly
RESULT=`psql -l | grep "gratefulmorningfarm" | wc -l | awk '{print $1}'`;
if test $RESULT -eq 0; then
    echo "Creating Database";
    psql -c "create role gratefulmorningfarm with createdb encrypted password 'gratefulmorningfarm' login;"
    psql -c "alter user gratefulmorningfarm superuser;"
    psql -c "create database gratefulmorningfarm with owner gratefulmorningfarm;"
else
    echo "Database exists"
fi

#run initial setup of database tables
poetry run python manage.py migrate
