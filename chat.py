import requests

text = input("Message: ")

url = input("URL:port: ")
route = input("Message URL route: ")
url2 = "http://" + url + "/" + route

message = {'message': f'{text}'}

response = requests.post(url2, json=message)

if response.status_code == 200:
    print("Message sent successfully!")
else:
    print("Failed to send the message.")
