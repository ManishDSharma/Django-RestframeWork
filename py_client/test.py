import json
import requests
import pprint

url = "http://100002.pythonanywhere.com/" 
#searchstring="ObjectId"+"("+"'"+"6139bd4969b0c91866e40551"+"'"+")"
payload = json.dumps({
  "cluster": "dowellconnection",
  "database": "dowellconnection",
  "collection": "connection_demo",
  "document": "connection_demo",
  "team_member_ID":"123456789",
  "function_ID": "ABCDE",
  "command": "insert",
  "field": {
    'test':"testing_dowellconnection"
  },
  "update_field": {
    "order_nos": 21
  },
  "platform": "bangalore"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)