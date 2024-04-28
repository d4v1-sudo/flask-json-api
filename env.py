import requests

url = input("URL:port: ")
env = input("Environment URL route: ")
url2 = "http://" + url + "/" + env

data = {'key': '1', 'value': 'coin'}

response = requests.post(url2, json=data)

if response.status_code == 201:
    print("Data sent successfully!")
else:
    print("Failed to send data.")
