import requests

url = input("URL:port: ")
route = input("GET URL route: ")
key = input("Key: ")
url2 = "http://" + url + "/" + route + "/" + key

response = requests.get(url2)

if response.status_code == 200:
    data = response.json()
    print("Received data:", data)
else:
    print("Failed to retrieve data.")
