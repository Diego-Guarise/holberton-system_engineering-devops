#!/usr/bin/python3
"""
recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], pag=""):
    """asd"""
    headers = {"User-Agent": "Mozilla/5.0"}
    url = 'https://www.reddit.com/r/' + subreddit +\
          '/hot.json?after={}'.format(pag)
    rh = requests.get(url, headers=headers, allow_redirects=False)
    if rh.status_code != 200:
        return None
    else:
        response = rh.json()
        tmp = response.get('data').get('children')
        for data in tmp:
            hot_list.append(data.get('data').get('title'))
        pag = response.get('data').get('after')
        if pag is not None:
            recurse(subreddit, hot_list, pag)
        return hot_list
