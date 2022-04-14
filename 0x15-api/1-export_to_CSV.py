#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import requests
from sys import argv


if __name__ == '__main__':
    id = int(argv[1])
    username = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{id}').json().get('username')
    req_tasks = requests.get(
        f'https://jsonplaceholder.typicode.com/todos?userId={id}').json()
    print.writeCSV({'filename': id, 'username': username, 'tasks': req_tasks})
