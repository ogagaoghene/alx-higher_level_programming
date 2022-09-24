#!/usr/bin/python3
"""Check status"""
import requests

def status():
    """status"""
    r = requests.get('https://intranet.hbtn.io/status', auth=('user', 'pass'))
    print("Body response:")
    print('\t- type: {}'.format(type(r.text)))
    print('\t- content: {}'.format(r.text))

if __name__ == "__main__":
    status()