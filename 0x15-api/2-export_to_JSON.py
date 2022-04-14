#!/usr/bin/python3

"""
export data in the JSON format information about 
his/her to-do list progress.
"""

import json
import requests
from sys import argv


if __name__ == '__main__':
    id = int(argv[1])
    username = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{id}').json().get('username')
    req_tasks = requests.get(
        f'https://jsonplaceholder.typicode.com/todos?userId={id}').json()
    with open(f"{id}.json", mode='w') as json_file:
        task_dct = {id: []}
        for tasks in req_tasks:
            task_dct[id] += [{'task': tasks['title'],
                              'completed': tasks['completed'], 'username': username}]
        data = json.dumps(task_dct)
        json_file.write(data)
