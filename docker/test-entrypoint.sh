#!/bin/bash

pip install -r requirements/test.txt
echo "Running pylint"
pylint -E weather_api/
if [[ $? != 0 ]]; then
    exit 1
else
    echo "Pylint doesn't find errors"
fi
coverage run --source='.' manage.py test
coverage report
