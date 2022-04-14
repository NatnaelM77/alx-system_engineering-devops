#!/usr/bin/python3

"""
Using a REST API, for a given employee ID and returns information
about his/her TODO list progress.
"""

import requests
from sys import argv


if __name__ == "__main__":
    todos = []
    id = int(argv[1])
    user = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{id}").json()
    req_todo = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={id}").json()
    for todo in req_todo:
        if todo.get("userId") == id and todo.get("completed"):
            todos += [todo.get("title")]
    print(f"Employee {user.get('name')} is done with tasks("
          f"{len(todos)}/{len(req_todo)})):")
    for task in todos:
        print("\t %s" % task)
