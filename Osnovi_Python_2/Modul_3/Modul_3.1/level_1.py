x, y, p = [int(input()) for _ in range(3)]

counter = 0
while x < y:
    x = int(x + x * (p / 100))
    counter += 1

print(counter)
