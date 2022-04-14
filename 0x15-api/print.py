#!/usr/bin/python3

"""
print formatted text
"""

import csv


def printf(user_info, tasks):
    """print text"""
    print(f"{user_info.get('name')} is done with tasks("
          f"{user_info.get('task')}/20):")
    if tasks:
        for task in tasks:
            print('\t %s' % task)


def writeCSV(dct={}):
    with open(f"{dct['filename']}.csv", mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_ALL)
        for row in dct['tasks']:
            csv_writer.writerow(
                [row['userId'], dct['username'], row['completed'], row['title']])
