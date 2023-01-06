import requests

uri_base = "https://web-production.lime.bike/api/rider/v1/views/map?"
params = {"ne_lat": "37.9"; "ne_lng": "-122"; "sw_lat": "37.7"; "sw_lng": "-122.4"; "user_latitude": "37.8"; "user_longitude": "-122.2"; "zoom": "50"}
uri_out = uri_base
for p in params:
    uri_out += p + "=" + params[p] + "&"
uri = uri_out[:-1]
header = {"authorization": "application/json"}
