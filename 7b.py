import math
from typing import Counter

f = open('./input/7.txt')

x_min = math.inf
x_max = 0
x_coords = Counter()

for s in f.readline().split(','):
    x = int(s)
    x_coords[x] += 1

    x_min = min(x, x_min)
    x_max = max(x, x_max)

"""
More one-liners!

In Maths™: min_{x_min \le i < x_max} sum_{x \in X} f(abs(x - i))
           f(x) = (x^2 + x) / 2

When you're making the cost function for x steps, you get
    f(x) = x + f(x - 1)
    f(0) = 0

If you work this out, you get the function as above, but damn, my
code got ugly. First, I wanted my code to be optimal, so I didn't
want to recalculate abs(x - i) for

    lambda i: ((abs(x - i)**2 + abs(x - i)) // 2) * x_coords[i]

One problem however:
You can pass it down to a different map, but then you would also
have to pass the x-value too, making it sub-optimal because you
have to construct a tuple each time. Ah well, this one looks a
lot nicer than

    map(lamba i: x_coords[i[1]] * (i[0]**2 + i[0]) // 2, map(lambda i: (abs(x - i), i), x_coords))

Look how ugly that is, almost as long as the current line. It is
a one liner though ¯\_(ツ)_/¯
"""

print(min(map(lambda x: sum(map(lambda i: ((abs(x - i)**2 + abs(x - i)) // 2) * x_coords[i], x_coords)), range(x_min, x_max))))