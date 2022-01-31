#!/usr/bin/python3
"""API"""


if __name__ == '__main__':
    import requests
    from sys import argv

    todos = 'https://jsonplaceholder.typicode.com/todos'
    users = 'https://jsonplaceholder.typicode.com/users'

    response1 = requests.get(todos)
    response2 = requests.get(users)

    users_json = response2.json()
    todos_json = response1.json()

    name = users_json[int(argv[1]) - 1]['username']

    donetask = 0
    tasks = 0
    dosome = []
    uid = int(argv[1])

    file = open('{}.CSV'.format(uid), 'w')

    for tmp in todos_json:
        if tmp['userId'] == uid:
            file.write('"{}","{}","{}","{}"\n'.format(
                uid, name, tmp['completed'], tmp['title']))
