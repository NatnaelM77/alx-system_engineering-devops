#!/usr/bin/python3
'''
Returns information about his/her to list progress.
'''
import requests
import sys

if __name__ == '__main__':
    todos = []
    id = int(sys.argv[1])
    user = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{id}').json()
    req_todo = requests.get(
        f'https://jsonplaceholder.typicode.com/todos?userId={id}').json()
    for todo in req_todo:
        if todo.get('userId') == id and todo.get('completed'):
            todos += [todo.get('title')]
    print(f'Employee {user.get("name")} is done with tasks('
          f'{len(todos)}/{len(req_todo)})):')
    for task in todos:
        print('\t %s' % task)
