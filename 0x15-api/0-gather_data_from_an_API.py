#!/usr/bin/python3

"""Returns to-do list information for a given employee ID."""

import json
from print import printf
import requests
from sys import argv

id = argv[1]
todos = []
req_user = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}')
user = json.loads(req_user.text).get('name')

req_todo = requests.get(f'https://jsonplaceholder.typicode.com/todos/')
res = json.loads(req_todo.text)

for todo in res:
    if todo.get('userId') == id and todo.get('completed'):
        todos += [todo.get('title')]

printf({'name': user, 'task': len(todos)}, todos)
