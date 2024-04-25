#!/usr/bin/python3
"""a Python script to export data in the CSV format"""

from requests import get
from sys import argv

if __name__ == '__main__':
    user_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    response = get(url)
    username = response.json().get('username')

    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)
    response = get(url)
    tasks = response.json()
    with open('{}.csv'.format(user_id), 'w') as fp:
        for task in tasks:
            fp.write('"{}","{}","{}","{}"\n'
                     .format(user_id, username,
                             task.get('completed'),
                             task.get('title')))
