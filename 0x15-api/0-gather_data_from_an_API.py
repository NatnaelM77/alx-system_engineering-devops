#!/usr/bin/python3

"""
for a given employee ID, returns information about his/her TODO list progress.
"""

import json
import requests
from sys import argv
from print import printf

id = argv[1]
todos = []
req = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}')
user = json.loads(req.text).get('name')

req = requests.get(f'https://jsonplaceholder.typicode.com/todos/')
res = json.loads(req.text)

for todo in res:
    if todo.get('userId') == id and todo.get('completed'):
        todos += [todo.get('title')]

printf({'name': user, 'task': len(todos)}, todos)
