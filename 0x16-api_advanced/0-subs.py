#!/usr/bin/python3
"""A function that Queries REDDIT API and returns the number
of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """This function returns 0 if an invalid subreddit
    is given""" 
    subscribe = 0
    headers = {'User-agent': 'Google Chrome Version 125.0.0.0'}
    url = 'https://www.reddit.com/r/' + subreddit + '/about.json'
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
       	info = response.jason().get('data')
	if info:
	   subscribe = info.get('subscriber')
	return subscribe 
