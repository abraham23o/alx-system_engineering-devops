#!/usr/bin/python3
"""a Python script to export data in JSON format"""
import json
from requests import get

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users/'
    response = get(url)
    users = response.json()

    my_dict = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
        url = url + '/todos'
        response = get(url)
        tasks = response.json()
        my_dict[user_id] = []
        for task in tasks:
            my_dict[user_id].append(
                {
                    "task": task.get('title'),
                    "completed": task.get('completed'),
                    "username": username
                }
            )
            with open('todo_all_employees.json', 'w') as fp:
                json.dump(my_dict, fp)
