import requests

url = "http://127.0.0.1:8000/api/location/"

payload={}
headers = {}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.json())
