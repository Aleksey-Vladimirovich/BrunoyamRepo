def register(login, passwd):
    # write in json file
    with open('users.json', 'w') as info:
        info.write(f'{login} {passwd}')
    return