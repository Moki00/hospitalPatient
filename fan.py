# s = session used to access api
def toggle_fan (s):
    print("Toggling Fans")
    # use 14 to read fan status
    url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/binary-value/14/properties/presentValue"
    resp = s.get(url, verify=False)
    
    fan_status = resp.json()['value']

    # use 13 to change status
    url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/binary-value/13/properties/presentValue"

    if fan_status == "Active":
        s.post(url, json={"value": "Inactive"})
        print("Off")
    else:    
        s.post(url, json={"value": "Active"})
        print("On")
        