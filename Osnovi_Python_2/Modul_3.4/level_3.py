def login_funtion(login, passwd):
    with open('users.txt', 'r', encoding='utf-8') as info:
        users = {i[0]: i[1] for i in j.split() for j in info.readlines()}
        if login not in users.keys():
            print('login does not exist')
            return False
        elif passwd != users[login]:
            print('wrong password')
            return False
        else:
            print('authorization successful')
            return True
