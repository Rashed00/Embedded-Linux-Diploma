#!/usr/bin/python3

import requests

def activity():
    activity = requests.get("https://www.boredapi.com/api/activity")
    if activity.status_code == 200:
        return activity.json()['activity']
    
print(activity())