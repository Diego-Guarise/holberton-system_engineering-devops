#!/usr/bin/python3
"""How many subs?"""


import requests


def number_of_subscribers(subreddit):
	"""
	function that queries the Reddit API 
	and returns the number of subscribers
	"""
	url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
	response = requests.get(url, headers={"User-Agent": "andydev_"},
							allow_redirects=False)
	if response.status_code == 200:
		return response.json().get("data").get("subscribers")
	else:
		return 0
