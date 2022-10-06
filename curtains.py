# s = session used to access api
def toggle_curtains (s):
    print('Toggling curtains')
    # use 17 to read fan status
    url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/binary-value/17/properties/presentValue"
    resp = s.get(url, verify=False)
    
    fan_status = resp.json()['value']

    # use 17 to change status
    url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/binary-value/17/properties/presentValue"

    if fan_status == "Active":
        s.post(url, json={"value": "Inactive"})
        print("Off")
    else:    
        s.post(url, json={"value": "Active"})
        print("On")
        