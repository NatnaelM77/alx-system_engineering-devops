#!/usr/bin/python3

"""
module that prints the titles of the first 10 hot posts
"""

import requests as req


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts listed for a given
    subreddit.
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    header = {'User-Agent': '0x16-api_advanced:1-top_ten:v1.0.0 (by '
                            '/u/natnaelm77)'}
    request = req.get(url, headers=header, allow_redirects=False)
    if request.status_code == 404:
        print("None")
        return
    request = request.json().get('data')
    for post in range(10):
        print(request.get('children')[post].get('data').get('title'))
