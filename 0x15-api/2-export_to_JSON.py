#!/usr/bin/python3
"""a Python script to export data in JSON format"""
import json
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

    my_dict = {user_id: []}

    for task in tasks:
        my_dict[user_id].append(
            {
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
            }
        )
    with open('{}.json'.format(user_id), 'w') as fp:
        json.dump(my_dict, fp)
