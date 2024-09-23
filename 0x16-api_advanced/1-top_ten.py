#!/usr/bin/python3
"""Get top 10 hot posts"""
import requests


def top_ten(subreddit):
    """Top 10 hot posts"""

    url = f'https://api.reddit.com/r/{subreddit}/hot?limit=10'

    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json().get('data', {}).get('children', [])
        for post in posts:
            print(post['data']['title'])
    else:
        print(None)
