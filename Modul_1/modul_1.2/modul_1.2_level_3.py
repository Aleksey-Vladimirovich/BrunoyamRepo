# level 3
while True:
    psw = input('введите пароль: ')
    if len(psw) > 8:
        if any(list(map(lambda x: x.isupper(), psw))) and \
           any(list(map(lambda x: x.islower(), psw))):
            print('допустимый пароль')
            break
        print('недопустимый пароль')
    print('недопустимый пароль')