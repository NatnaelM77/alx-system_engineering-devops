#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import json
import print
import requests
import sys

if __name__ == '__main__':
    id = int(sys.argv[1])
    todos = []
    req_user = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{id}')
    user = json.loads(req_user.text).get('name')

    req_todo = requests.get(f'https://jsonplaceholder.typicode.com/todos/')
    res = json.loads(req_todo.text)

    for todo in res:
        if todo.get('userId') == id and todo.get('completed'):
            todos += [todo.get('title')]

    print.printf({'name': user, 'task': len(todos)}, todos)
