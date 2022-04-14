#!/usr/bin/python3
"""returns information about his/her to-do list progress.
"""


import json
import requests
from sys import argv


def printf(user_info, tasks):
    print(f"{user_info.get('name')} is done with tasks("
          f"{user_info.get('task')}/20):")
    if tasks:
        for task in tasks:
            print('\t %s' % task)


if __name__ == '__main__':
    id = int(argv[1])
    todos = []
    req_user = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{id}')
    user = json.loads(req_user.text).get('name')

    req_todo = requests.get(f'https://jsonplaceholder.typicode.com/todos/')
    res = json.loads(req_todo.text)

    for todo in res:
        if todo.get('userId') == id and todo.get('completed'):
            todos += [todo.get('title')]

    printf({'name': user, 'task': len(todos)}, todos)
