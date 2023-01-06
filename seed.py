import requests

uri = 'https://web-production.lime.bike/api/rider/v1/login'
header = 'Content-Type: application/json'
data = '{"login_code": "242257", "phone": "+17045176027"}'


response = requests.get("https://web-production.lime.bike/api/rider/v1/login?phone=%2B33612345678")
