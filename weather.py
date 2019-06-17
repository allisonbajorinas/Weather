from flask import Flask, render_template
#from flask import request
import requests
import json

app = Flask(__name__)



@app.route('/')
def hello():
    return "Hello World"

@app.route('/mytest')
def mytest1():
    return "Test"

@app.route('/weather2')
def weather2():
    payload = {'zip':'06468','APPID':'14988a919884e2428d46e52e27447c0b'}
    return json.dumps(payload)

@app.route('/myweather')
def getweather():
    payload = {'zip':'06468','APPID':'14988a919884e2428d46e52e27447c0b'}
    data = requests.get('https://api.openweathermap.org/data/2.5/weather',params=payload)
    return data.text

@app.route('/zip/<postalcode>', methods=['GET'])
def weather(postalcode):
    payload = {'zip': postalcode,'APPID':'14988a919884e2428d46e52e27447c0b'}
    data = requests.get('https://api.openweathermap.org/data/2.5/weather',params=payload)
    jdata = data.json()
    rdata = jdata['main']['temp']
    return str(rdata)

# weather addition / testing github

