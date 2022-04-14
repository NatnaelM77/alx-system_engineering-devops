#!/usr/bin/python3

"""
export data in the JSON format information about his/her to-do list progress.
"""

import json
from print import printf, writeCSV, writeJSON
import requests
from sys import argv

if __name__ == '__main__':
    todos = []
    id = int(argv[1])
    req_user = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{id}')
    username = json.loads(req_user.text).get('username')

    req_tasks = requests.get(
        f'https://jsonplaceholder.typicode.com/todos?userId={id}')
    res_tasks = json.loads(req_tasks.text)

    writeJSON({
        'filename': id,
        'username': username,
        'tasks': res_tasks
    })
