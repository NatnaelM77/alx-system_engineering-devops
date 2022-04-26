#!/usr/bin/python3

"""
module that returns the number of subscribers.
"""

import requests as req


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    header = {'User-Agent': '0x16-api_advanced:0-subs:v1.0.0 (by '
                            '/u/natnaelm77)'}
    if subreddit is None or type(subreddit) is not str:
        return 0
    request = req.get(url, headers=header).json()
    subscribers = request.get('data').get('subscribers')
    return subscribers
