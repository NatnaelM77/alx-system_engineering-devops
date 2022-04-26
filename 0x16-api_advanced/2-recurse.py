#!/usr/bin/python3

"""
module that returns a list containing the titles of all hot articles
"""

import requests as req


def recurse(subreddit, hot_list=[], after=None):
    """returns a list containing the titles of all hot articles for a given
    subreddit.
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    header = {'User-Agent': '0x16-api_advanced:2-recurse:v1.0.0 (by '
                            '/u/natnaelm77)'}
    request = req.get(url, headers=header, params={'after': after},
                      allow_redirects=False)
    if request.status_code == 404:
        return None
    request = request.json().get('data')
    after = request.get('after', None)
    hot_list.append(post.get('data').get('title') for post in request.get(
            'children'))
    if after is not None:
        return recurse(subreddit, hot_list, after)
    else:
        if len(hot_list) == 0:
            return None
        return hot_list
