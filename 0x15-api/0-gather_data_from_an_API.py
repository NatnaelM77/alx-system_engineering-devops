#!/usr/bin/python3
"""returns information about his/her to-do list progress."""

import print
import requests
from sys import argv


if __name__ == '__main__':
    todos = []
    id = int(argv[1])
    user = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{id}').json().get('name')
    req_todo = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={id}").json()
    for todo in req_todo:
        if todo.get('userId') == id and todo.get('completed'):
            todos += [todo.get('title')]
    print.printf({'name': user, 'task': len(todos),
           'task_completed': len(req_todo)}, todos)
