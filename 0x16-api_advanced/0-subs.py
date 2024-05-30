#!/usr/bin/python3
"""
Fetch the subs in a subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    Fetch the subs in a subreddit
    :param subreddit: subreddit o find subs for
    :return: 0 if false, else no. of subs
    """
    url = f'https://api.reddit.com/r/{subreddit}/about'
    headers = {'User-Agent': 'adari-corp'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json() or {}
        return data.get('data', {}).get('subscribers', 0)
    return 0
