import requests

uri = 'https://web-production.lime.bike/api/rider/v1/login'
header = {"Content-Type": "application/json"}
data = '{"login_code": "424062", "phone": "+17045176027"}'


response = requests.post(uri, data=data, headers=header)
print(response, type(response), response.text, response.json)
