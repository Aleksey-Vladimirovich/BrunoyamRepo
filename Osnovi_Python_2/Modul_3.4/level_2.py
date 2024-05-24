def register(login:str, passwd:str) -> None:
    # write in json file
    with open('users.json', 'r', encoding='utf-8') as info:
        user_info = {i[0]:i[1] for i in j.split() for j in info.readlines()}
        if login in user_info.keys():
            print('login already exists')
            return False
        else:
            with open('users.json', 'a') as info:
                info.write(f'\n{login} {passwd}')
                print('successful registration')
            return True