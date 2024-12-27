#!/bin/bash 
# script to generate migrations

# flask db init  # run once
read -p "Enter migration message: " message
flask db migrate -m "$message"  # Create migration scripts for your current models
flask db upgrade