import math
from typing import Counter

f = open('./input/7.txt')

"""
I was on a Maths™ roll and I wanted to make the x_min MATHEMATICALLY
the minimum, you can never be sure enough! Maybe M IS your minimum
value!
"""
x_min = math.inf
x_max = 0

x_coords = Counter()

for s in f.readline().split(','):
    x = int(s)
    x_coords[x] += 1

    x_min = min(x, x_min)
    x_max = max(x, x_max)

"""
Python one-liners! You gotta love them!

In Maths™: min_{x_min \le i < x_max} sum_{x \in X} abs(x - i)

Since x_coords is a Counter, we can iterate over it and get
the indices (x-coordinates), and the counter value being the
amount of crab submarines on that x-coordinate. that's why
we have that weird abs(x - i) * x_coords[i].
"""

print(min(map(lambda x: sum(map(lambda i: abs(x - i) * x_coords[i], x_coords)), range(x_min, x_max))))