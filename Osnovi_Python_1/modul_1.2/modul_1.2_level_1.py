# level 1
a = int(input('первое число: '))
b = int(input('второе число: '))
c = int(input('третье число: '))

if a == b or b == c:
    if a == c:
        print(3)
    else:
        print(2)
elif a == c:
    print(2)
else:
    print(0)