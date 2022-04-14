#!/usr/bin/python3
"""getting data from an api
"""

import requests
from sys import argv


def printf(user_info, tasks):
    print(f"{user_info.get('name')} is done with tasks("
          f"{user_info.get('task')}/{user_info.get('task_completed')}):")
    if tasks:
        for task in tasks:
            print('\t %s' % task)


if __name__ == '__main__':
    todos = []
    id = int(argv[1])
    req_user = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{id}').json()
    user = req_user.get('name')

    req_todo = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={id}").json()

    for todo in req_todo:
        if todo.get('userId') == id and todo.get('completed'):
            todos += [todo.get('title')]

    printf({'name': user, 'task': len(todos),
           'task_completed': len(req_todo)}, todos)
