import math

f = open('./input/7.txt')

x_min = math.inf
x_max = 0
numbers = []

for s in f.readline().split(','):
    x = int(s)
    numbers.append(x)

    x_min = min(x, x_min)
    x_max = max(x, x_max)

min_value = math.inf

for x in range(x_min, x_max):
    x_value = sum(map(lambda x: (x**2 + x) // 2, map(lambda n: abs(x - n), numbers)))
    if x_value < min_value:
        min_value = x_value

print(min_value)