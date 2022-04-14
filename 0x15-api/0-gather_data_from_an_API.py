#!/usr/bin/python3
"""
Using a REST API, for a given employee ID and returns information
about his/her to-do list progress.
"""

import requests
import sys


def printf(user_info, tasks):
    print(f"Employee {user_info.get('name')} is done with tasks("
          f"{user_info.get('task')}/20):")
    if tasks:
        for task in tasks:
            print('\t %s' % task)


if __name__ == '__main__':
    todos = []
    id = int(sys.argv[1])
    user = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{id}').json().get('name')
    req_todo = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={id}").json()
    for todo in req_todo:
        if todo.get('userId') == id and todo.get('completed'):
            todos += [todo.get('title')]
    printf({'name': user, 'task': len(todos),
                  'task_completed': len(req_todo)}, todos)
