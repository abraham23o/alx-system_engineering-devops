#!/usr/bin/python3
"""
2-recurse
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """a recursive function that queries the Reddit API and returns
    a list containing the titles of all hot articles
    for a given subreddit
    """
    url = f'https://api.reddit.com/r/{subreddit}/hot'
    headers = {'User-Agent': 'adari-corp'}
    params = {
        'limit': 100,
        'after': after
    }

    response = requests.get(url, params, headers=headers,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        hot_list.extend([post['data']['title'] for
                         post in data['data']['children']])
        after = data['data'].get('after')
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list

    elif response.status_code == 404:
        return None

    else:
        return None
