#!/usr/bin/python3
"""
a recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given
subreddit. If no results are found for the given subreddit, the
function should return None.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursive function that queries the Reddit API to get the titles
    of the hot posts

    :param subreddit: The name of the subreddit to fetch posts from
    :param hot_list: A list that accumulates the post titles
    (defaults to an empty list)
    :param after: parameter is used to get the next page of results.
    If it’s None, it fetches the first page.
    :return: a list containing the titles of all hot articles for a given
    subreddit. If no results are found for the given subreddit, the
    function should return None
    """
    url = f'https://api.reddit.com/r/{subreddit}/hot'

    # Custom User-Agent (important for API requests to Reddit)
    #headers = {'User-Agent': 'python-requests/2.32.3'}

    # Add the `after` parameter for pagination if it's not None
    params = {'after': after}

    # Send the GET request to the Reddit API
    response = (requests.get
                (url,
                 params=params,
                 allow_redirects=False))

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        response_data = response.json().get('data', {})

        # Get the pagination token for the next batch
        after = response_data.get('after')

        # Get the list of hot posts
        posts = response_data.get('children', [])

        # Append the titles of the posts to the hot_list
        hot_list.extend(post['data']['title'] for post in posts)

        """
        Recursively call the function if there are more posts
        (i.e., if `after` is not None)
        """
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            # No more posts, return the complete list of titles
            return hot_list
    else:
        # If the subreddit is invalid or the request failed, return None
        return None
