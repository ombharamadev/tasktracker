import requests

url = "http://localhost:8000/api/register"

header = {
    "User-Agent":"Nasa"
}

body = {
    "name":"aryan",
    "email":"jaswalaryan@proton.me",
    "passw":"12345678"
}

data = requests.post(url,headers=header,data=body)
print(data)
print(data.text)