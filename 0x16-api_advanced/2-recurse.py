#!/usr/bin/python3
"""Top Ten"""


import requests


def top_ten(subreddit):
    """
     function that queries the Reddit API and prints the
     titles of the first 10 hot posts listed for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, headers={"User-Agent": "andydev_"},
                            allow_redirects=False, params={"limit": 10})
    if response.status_code == 200:
        list = response.json().get("data").get("children")
        for item in list:
            print(item.get("data").get("title"))
    else:
        print("None")
