#!/usr/bin/python3

"""
export data in the JSON format information about his/her to-do list progress.
"""

import print
import requests
from sys import argv


if __name__ == '__main__':
    id = int(argv[1])
    username = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{id}').json().get('username')
    req_tasks = requests.get(
        f'https://jsonplaceholder.typicode.com/todos?userId={id}').json()
    print.writeJSON({'filename': id, 'username': username, 'tasks': req_tasks})
