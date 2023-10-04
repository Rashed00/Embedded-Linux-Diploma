#!/usr/bin/python3

import firelink

site = input("Choose site (facebook, google, youtube): ")
site = site.lower().strip()

firelink.google(f"www.{site}.com")
