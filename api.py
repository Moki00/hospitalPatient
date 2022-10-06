import requests
import json
from decimal import Decimal

import urllib3
urllib3.disable_warnings()

# Define the url access point for the api
device_ip = "10.50.241.5"
url = "https://" + device_ip + "/api/rest/v1/info/device"

username = 'team3'
password = "ChallengeTeam3"

# Create requests session
s = requests.Session()
s.verify = False

# Set authorization
s.auth = (username, password)

# Changing Light Dim

url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/analog-value/15/properties/presentValue"
resp = s.get(url, verify=False)
print(resp)
print(resp.json())

url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/analog-value/16/properties/presentValue"
s.post(url, 
    json={"value": "0.8"})

url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/analog-value/15/properties/presentValue"
resp2 = s.get(url, verify=False)
print(resp2)
print(resp2.json())

exit(0)

# Change Space Temperature and Space Temperature Control

url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/analog-value/13/properties/presentValue"
resp = s.get(url, verify=False)
print(resp)
print(resp.json())

url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/analog-value/14/properties/presentValue"
resp = s.get(url, verify=False)
print(resp)
print(resp.json())

current_temp = Decimal(resp.json()['value'])

url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/analog-value/13/properties/presentValue"
s.post(url, 
    json={"value": '13.13'})

url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/analog-value/14/properties/presentValue"
s.post(url, 
    json={"value": '14.14'})

url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/analog-value/13/properties/presentValue"
resp = s.get(url, verify=False)
print(resp)
print(resp.json())

url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/analog-value/14/properties/presentValue"
resp2 = s.get(url, verify=False)
print(resp2)
print(resp2.json())

exit(0)

# Changing Curtains

url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/binary-value/17/properties/presentValue"
resp = s.get(url, verify=False)
print(resp)
print(resp.json())

url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/binary-value/17/properties/presentValue"
s.post(url, 
    json={"value": "Active"})

url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/binary-value/17/properties/presentValue"
resp2 = s.get(url, verify=False)
print(resp2)
print(resp2.json())

exit(0)

# See and change light status
# change 15 and 16 to 13 and 14 for fan status

url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/binary-value/16/properties/presentValue"
resp = s.get(url, verify=False)
print(resp)
print(resp.json())

url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/binary-value/15/properties/presentValue"
s.post(url, 
    json={"value": "Active"})

url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/binary-value/16/properties/presentValue"
resp2 = s.get(url, verify=False)
print(resp2)
print(resp2.json())

exit(0)

# See all api endpoints for url

resp = s.get(url, verify=False)

print(resp)
resp_json = resp.json()
for e in resp_json:
    print(e['name'])
    resp2 = s.get(url + e['name'], verify=False)
    resp2_json = resp2.json()
    print(resp2_json)
    print("======================================================")
#print(json.dumps(resp_json, indent=2))

exit(0)

# See all devices

print("Binary Value")
for i in range(13, 18):
    # Send request
    url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/binary-value/" + str(i) +  "/properties/object-name"
    resp = s.get(url, verify=False)

    # print response
    #print(resp)
    #print(resp.text)
    #print(resp.cookies)
    #print("===============================================")

    print(str(i) + " " + resp.json()['value'])

    #print("===============================================")

    # print cookie
    #print(s.cookies)

print("================================================================")
print("Analog Value")
for i in range(13, 18):
    # Send request
    url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/analog-value/" + str(i) +  "/properties/object-name"
    resp = s.get(url, verify=False)

    # print response
    #print(resp)
    #print(resp.text)
    #print(resp.cookies)
    #print("===============================================")

    print(str(i) + " " + resp.json()['value'])

    #print("===============================================")

    # print cookie
    #print(s.cookies)

print("================================================================")
print("Multi State Value")

url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/multistateValue/3/properties/object-name"
resp = s.get(url, verify=False)

# print response
#print(resp)
#print(resp.text)
#print(resp.cookies)
#print("===============================================")

print("3 " + resp.json()['value'])
