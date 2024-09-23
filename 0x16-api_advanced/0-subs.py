#!/usr/bin/python3

"""
returns the number of subscribers (not active users,
total subscribers) for a given subreddit. If an invalid
subreddit is given, the function should return 0
"""

import requests


def number_of_subscribers(subreddit):
    """Fetch reddit subs"""
    url = f'https://api.reddit.com/r/{subreddit}/about'
    headers = {'User-Agent': 'api_advanced/0-subs (by u/adari'}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json() or {}
        return data.get('data', {}).get('subscribers', 0)
    return 0
