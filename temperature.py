# s = session used to access api
# returns current temeprature (in Fahrenheit) as a double
def get_temperature (s):
    url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/analog-value/13/properties/presentValue"
    resp = s.get(url, verify=False)
    return resp.json()['value']

# Sets the temperature
# new_temp is a double
# s = session used to access api
def set_temperature (s, new_temp):
    print("Setting temeperature to " + str(new_temp))
    url = "https://10.50.241.5/api/rest/v1/protocols/bacnet/local/objects/analog-value/14/properties/presentValue"
    s.post(url, json={"value": str(new_temp)})
    