#!/usr/bin/python3

"""
module that prints counts of given words found in hot posts
"""

import requests as req

def count_words(subreddit, word_list):
    """Prints counts of given words found in hot posts of a given subreddit.
       Args:
           subreddit (str): The subreddit to search.
           word_list (list): The list of words to search for in post titles.
           found_list (obj): Key/value pairs of words/counts.
           after (str): The parameter for the next page of the API results.
    """
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(subreddit,
                                                                 after)
    header = {'User-Agent': '0x16-api_advanced:100-count:v1.0.0 (by '
                            '/u/natnaelm77)'}
    posts = req.get(url, headers=header, params=params,
                      allow_redirects=False)

    if after is None:
        word_list = [word.lower() for word in word_list]

    if posts.status_code == 200:
        posts = posts.json()['data']
        aft = posts['after']
        posts = posts['children']
        for post in posts:
            title = post['data']['title'].lower()
            for word in title.split(' '):
                if word in word_list:
                    found_list.append(word)
        if aft is not None:
            count_words(subreddit, word_list, found_list, aft)
        else:
            result = {}
            for word in found_list:
                if word.lower() in result.keys():
                    result[word.lower()] += 1
                else:
                    result[word.lower()] = 1
            for key, value in sorted(result.items(), key=lambda item: item[1],
                                     reverse=True):
                print('{}: {}'.format(key, value))
    else:
        return

