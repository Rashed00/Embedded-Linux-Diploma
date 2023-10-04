#!/usr/bin/python3
import requests
import json

IP = requests.get("https://api.ipify.org/?format=json")
if IP.status_code == 200:
    IP = IP.json()['ip']

need = ['country', 'loc']
Location = requests.get(f"https://ipinfo.io/{IP}/geo")
if Location.status_code == 200:
    print(json.dumps(Location.json(),indent=0))
    print(type(json.dumps(Location.json())))

