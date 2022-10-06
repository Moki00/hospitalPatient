from flask import Flask, render_template, Response, request, redirect, url_for
import curtains, fan, light_cmd, temperature
import os
import requests

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

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/call")
def call():
    return render_template("/call/call.html")

@app.route("/body")
def body():
    return render_template("/body/body.html")

@app.route("/emergency")
def emergency():
    return render_template("/call/emergency.html")

# room
@app.route("/room")
def room():
    return render_template("/room/room.html")

# shutter
@app.route("/shutter")
def shutter():
    return render_template("/room/shutter.html")

@app.route("/toggle_curtains")
def toggle_curtains():
    curtains.toggle_curtains(s)
    return render_template("/room/shutter.html")

# fan
@app.route("/toggle_fan")
def toggle_fan():
    fan.toggle_fan(s)
    return render_template("/room/ac.html")

@app.route("/toggle_lights")
def toggle_lights():
    light_cmd.toggle_light(s)
    return render_template("/room/lights.html")

# lights
@app.route("/lights")
def lights():
    return render_template("/room/lights.html")

# bed
@app.route("/bed")
def bed():
    return render_template("/room/bed.html")

# fan for ac and heater
@app.route("/ac")
def ac():
    return render_template("/room/ac.html")

# temperature
@app.route("/temperature")
def temperature():
    return render_template("/room/temp.html")

@app.route('/your_flask_route')
def your_flask_route():
    os.system("python hello.py")
    return "done"

    
if __name__ == "__main__":
    app.run(debug=True)
    #app.run(debug=True, host = '10.50.241.23')
    #We made two new changes
