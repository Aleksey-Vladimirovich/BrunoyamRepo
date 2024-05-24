from random import randint

n = int(input())
matrix = [[randint(0, 100) for _ in range(n)] for _ in range(n)]
for row in matrix:
    print(*row)
print()

mx = -1
for row in matrix:
    mx = max(mx, max(row))

print(mx)
