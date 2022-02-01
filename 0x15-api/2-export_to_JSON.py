#!/usr/bin/python3
"""API"""


if __name__ == '__main__':
    import json
    import requests
    from sys import argv

    todos = 'https://jsonplaceholder.typicode.com/todos'
    users = 'https://jsonplaceholder.typicode.com/users'

    response1 = requests.get(todos)
    response2 = requests.get(users)

    users_json = response2.json()
    todos_json = response1.json()

    name = users_json[int(argv[1]) - 1]['username']

    dosome = []
    uid = argv[1]
    dic = {}
    lista = []
    for tmp in todos_json:
        if tmp['userId'] == int(uid):
            tmp['task'] = tmp.pop('title')
            tmp['username'] = name
            del tmp['id']
            del tmp['userId']
            lista.append(tmp)
    dic[str(uid)] = lista

    with open('{}.json'.format(uid), 'w') as f:
        json.dump(dic, f)
