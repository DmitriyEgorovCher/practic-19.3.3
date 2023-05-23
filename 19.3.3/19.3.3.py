import requests
import json

status='available'
baseURL = "https://petstore.swagger.io/v2"

#GET Запрос
res = requests.get(f"{baseURL}/pet/findByStatus?status={status}", headers = {'accept': 'application/json', })

print(res.text)
print(res.status_code)
print(res.json())
print(type(res.json()))
print('////////////////////////////////////////////////')


#POST Запрос
date = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
date = json.dumps(date)
res = requests.post(f"{baseURL}/pet", headers={'Content-Type': 'application/json', 'accept': 'application/json'},
data=date)

print(res.text)
print(res.status_code)
print(res.json())
print(type(res.json()))
print('////////////////////////////////////////////////')

#PUT Запрос
date = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "kitten",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
date = json.dumps(date)
res = requests.put(f"{baseURL}/pet", headers={'Content-Type': 'application/json', 'accept': 'application/json'},
data=date)

print(res.text)
print(res.status_code)
print(res.json())
print(type(res.json()))
print('////////////////////////////////////////////////')


#DELET Запрос
petID = 9223372036854629917
res = requests.delete(f"{baseURL}/pet/{petID}")

print(res.text)
print(res.status_code)
print(res.json())
print(type(res.json()))