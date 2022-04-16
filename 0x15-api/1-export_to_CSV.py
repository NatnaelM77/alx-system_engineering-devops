#!/usr/bin/python3

"""
Exports to-do list information for a given employee
ID to CSV format.
"""

import csv
import requests
from sys import argv


if __name__ == "__main__":
    todos = []
    user_id = int(argv[1])
    base_url = "https://jsonplaceholder.typicode.com/"
    username = requests.get("{}users/{}".format(base_url, user_id)).json().get("username")
    req_tasks = requests.get("{base_url}todos", params={"user_id": user_id}).json()
    with open(f"{id}.csv", mode="w") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",",
                                quotechar='"', quoting=csv.QUOTE_ALL)
        for row in req_tasks:
            csv_writer.writerow(
                [row["userId"], username, row["completed"], row["title"]])
