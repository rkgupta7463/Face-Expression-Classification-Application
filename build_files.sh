#!/bin/bash

# Print a message indicating the start of the build
echo "BUILD START"

# Install Python dependencies from requirements.txt
python3.11 -m pip install -r requirements.txt

# Print a message indicating the start of the build
# echo "COLLECTING STATIC FILES"

# Collect static files (adjust the command as needed)
# python3.11 manage.py collectstatic --noinput --clear

# Print a message indicating the end of the build
echo "BUILD END"
