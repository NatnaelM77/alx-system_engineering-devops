#!/usr/bin/python3
"""
Returns information about his/her to list progress.
"""
import requests
from sys import argv

if __name__ == "__main__":
    todos = []
    base_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(f"{base_url}/users{argv[1]}").json()
    req_todo = requests.get(f"{base_url}/todos?userId={argv[1]}").json()
    for todo in req_todo:
        if todo.get("userId") == id and todo.get("completed"):
            todos += [todo.get("title")]
    print(f"Employee {user.get('name')} is done with tasks("
          f"{len(todos)}/{len(req_todo)})):")
    for task in todos:
        print("\t %s" % task)
