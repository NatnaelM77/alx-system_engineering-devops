#!/usr/bin/python3

"""
returns information about his/her to-do list progress.
"""


import requests
from sys import argv


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
