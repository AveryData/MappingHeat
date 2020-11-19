#!/usr/bin/env bash

# Unzip compressed data
echo  "Unziping data"
unzip $PWD/instance/mapping_heat.sqlite.zip -d $PWD/instance/
unzip $PWD/mapping_heat/fixtures/pitching_data.csv.zip -d $PWD/mapping_heat/fixtures/

# Install packages
echo "Install requirments"
pip3 install -r $PWD/requirements.txt

# Export flask env vars
echo "Set Env Vars"
export FLASK_APP=mapping_heat
export FLASK_ENV=development

# Init the database
echo "Init Database"
flask init-db


# Move to mapping_heat dir
#echo "Moving into application diretory"
#cd mapping_heat

# Run the backend
echo "Starting Server"
flask run

