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

    name = users_json[int(argv[1]) - 1]['name']

    donetask = 0
    tasks = 0
    dosome = []
    uid = int(argv[1])
    for tmp in todos_json:
        if tmp['userId'] == uid:
            if tmp['completed'] is True:
                donetask = donetask + 1
                dosome.append(tmp['title'])
            tasks = tasks + 1

    print('Employee {} is done with tasks({}/{}):'.format(
        name, donetask, tasks))
    for TASK_TITLE in dosome:
        print('\t {}'.format(TASK_TITLE))
