#!/usr/bin/python3

'''
Exports to-do list information for a given employee
ID to CSV format.
'''

import csv
import requests
from sys import argv


if __name__ == '__main__':
    id = int(argv[1])
    username = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{id}').json().get('username')
    req_tasks = requests.get(
        f'https://jsonplaceholder.typicode.com/todos?userId={id}').json()
    with open(f"{id}.csv", mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_ALL)
        for row in req_tasks:
            csv_writer.writerow(
                [row['userId'], username, row['completed'], row['title']])
