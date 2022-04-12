#!/usr/bin/python3

"""
print formatted text
"""


def printf(user_info, tasks):
    """print text"""
    print(f"{user_info.get('name')} is done with tasks("
          f"{user_info.get('task')}/20):")
    if tasks:
        for task in tasks:
            print('\t %s' % task)
