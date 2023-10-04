#!/usr/bin/python3
import webbrowser

def firefox(url):
    webbrowser.open_new(url)
    
def google(url):
    webbrowser.get("google-chrome").open_new(url)
    
# facebook_link = "www.facebook.com"
# google_link = "www.google.com"
# youtube_link = "www.youtube.com"