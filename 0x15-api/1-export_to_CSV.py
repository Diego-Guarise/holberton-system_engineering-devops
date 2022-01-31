#!/usr/bin/python3
"""API"""


if __name__ == '__main__':
    import csv
    import requests
    from sys import argv

    todos = 'https://jsonplaceholder.typicode.com/todos'
    users = 'https://jsonplaceholder.typicode.com/users'

    response1 = requests.get(todos)
    response2 = requests.get(users)

    users_json = response2.json()
    todos_json = response1.json()

    name = users_json[int(argv[1]) - 1]['username']

    uid = int(argv[1])
    line = [uid, name, '', '']
    with open('{}.csv'.format(uid), 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)

        for tmp in todos_json:
            if tmp['userId'] == uid:
                if tmp['completed'] is True:
                    completed = 'True'
                else:
                    completed = 'False'
                line[2] = completed
                line[3] = tmp['title']
                writer.writerow(line)
