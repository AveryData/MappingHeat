# Mapping Heat

## Description
Mapping Heat is a project dedicated to understanding the data behind MLB pitchers better. It aims to help baseball professionals make better, more informed choices, and as well the average fan enjoy and play scenarios with their favorite pitchers.

It's a simple visualization that display hit probabilities on a static heat map with a selected pitcher and pitch type. The probabilities are calculated via logistic regression and the visulazation is controlled via D3.

The package include several aspects: the 2020 season data, scripts to create the SQLite database, scripts to train the models, and finally scripts to create the data visualization.

## Installation
- Download entire package from GitHub
- `cd` into backend directory
- Go to the 'instance' folder and unzip mapping_heat.sqlite.zip
- Go to the 'fixtures' folder and unzip pitching_data.csv.zip
- Ensure you have unzipped the proper files before moving on
- Ensure you all the proper packages, 'pip install -r requirements.txt'
- Run `flask init-db` to initialize the SQLite data base
- After these steps, the package is downloaded and ready to return

## Execution
- From the backend folder, 'export FLASK_APP=mapping_heat'
- From the backend folder, 'export FLASK_ENV=development'
- Run `flask run` which will launch the backend process
- In a separate terminal, launch a local HTTP server via 'python3 -m http.server 8000'
- Open 'http://0.0.0.0:8000/pitch_v1.html'in a browser of choice and the visual should be live



### Hit endpoints
- pitcher endpoint
  -  ` curl  http://127.0.0.1:5000/stats/pitcher?name=Brad%20Hand | jq .`
- pitch type endpoint
  - `curl  "http://127.0.0.1:5000/stats/pitcher/pitch?name=Brad%20Hand&pitch=FF" | jq .`
- pitch feature endpoint
  - ` curl "http://127.0.0.1:5000/stats/pitcher?name=Brad%20Hand&feature=release_speed&value=78.7" | jq .`
