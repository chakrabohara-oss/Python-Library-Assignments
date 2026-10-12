import requests

url = "https://httpbin.org/get"

response = requests.get(url, timeout=10)

print("Status code:", response.ststus_code)
print("Response data:")
print(response.json())