# Flask Backend 

TODO:
- Send data to frontend
- Endpoint to cal probabilities 

### Setup application 
- `cd` into backend directory 
- unzip mapping_heat.sqlite.zip & pitching_data.csv.zip
- run `flask init-db`
- run `flask run`

### Hit endpoints 
- pitcher endpoint 
  -  ` curl  http://127.0.0.1:5000/stats/pitcher?name=Brad%20Hand | jq .`
- pitch type endpoint
  - `curl  "http://127.0.0.1:5000/stats/pitcher/pitch?name=Brad%20Hand&pitch=FF" | jq .`
- pitch feature endpoint
  - ` curl "http://127.0.0.1:5000/stats/pitcher?name=Brad%20Hand&feature=release_speed&value=78.7" | jq .`
