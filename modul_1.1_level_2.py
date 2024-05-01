# level 2
s = 109
v = int(input('скорость: '))
t = int(input('время: '))

print(v * t if v * t < s else v * t % s)