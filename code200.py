#!/usr/bin/python

import requests
import os
from dotenv import load_dotenv

def get_http_code(url):
    response = requests.get(url)
    return response.status_code

load_dotenv()
url = os.getenv("URL")

print(get_http_code(url))