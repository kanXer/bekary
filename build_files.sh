#!/bin/bash

echo "BUILD START"

# Install Django and project dependencies
python3.9 -m pip install -r requirements.txt

# Collect static files
python3.9 manage.py collectstatic --noinput --clear

echo "BUILD END"
