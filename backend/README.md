# Flask Backend

TODO:
- Send data to frontend
- Endpoint to cal probabilities

### Setup application
- `cd` into backend directory
- unzip mapping_heat.sqlite.zip & (go to fixtures) pitching_data.csv.zip
- from the backend folder, 'export FLASK_APP=mapping_heat'
- from the backend folder, 'export FLASK_ENV=development'
- You may have to pip install some more modules
- run `flask init-db`
- run `flask run`

### Hit endpoints
- pitcher endpoint
  -  ` curl  http://127.0.0.1:5000/stats/pitcher?name=Brad%20Hand | jq .`
- pitch type endpoint
  - `curl  "http://127.0.0.1:5000/stats/pitcher/pitch?name=Brad%20Hand&pitch=FF" | jq .`
- pitch feature endpoint
  - ` curl "http://127.0.0.1:5000/stats/pitcher?name=Brad%20Hand&feature=release_speed&value=78.7" | jq .`
