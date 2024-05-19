# level 2
x1, y1 = int(input()), int(input())
x2, y2 = int(input()), int(input())

if x1 == x2 or x1 == y2 or y1 == x1 or y1 == y2:
    print('YES')
else:
    print('NO')