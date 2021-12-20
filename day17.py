(x_min, x_max), (y_min, y_max) = list(map(lambda i: list(map(int, i[2:].split('..'))), open('./input/17.txt').read()[13:].split(', ')))

###############
print('part 1')
###############

"""
If we only look at the y trajectory, we find a simple
parabola: the derivative is linear per step. To maximize
the peek, we have to find the point of landing, farthest
away from the x-axis. 0 is not gonna be in the y-range,
because else there is no limit on the power. That's
why we assume sgn(y_min) == sgn(y_max). One problem: if
the intersection is below zero, we will have to take the
extra step into account, so y_dir = -(y_min - 1).
"""

y_dir_max = y_max if y_max > 0 else -y_min - 1

print((y_dir_max ** 2 + y_dir_max) // 2)

###############
print('part 2')
###############

def fire_probe(x_dir, y_dir):
    x, y = 0, 0

    while x <= x_max and y >= y_min:
        x += x_dir
        y += y_dir

        if  x in range(x_min, x_max + 1)\
        and y in range(y_min, y_max + 1):
            return True

        x_dir = max(0, x_dir - 1)
        y_dir -= 1
    
    return False

x_lb = min(x for x in range(x_min + 1) if (x**2 + x) // 2 >= x_min)
x_ub = x_max

y_lb = y_min if y_min < 0 else min(y for y in range(y_min + 1) if (y**2 + y) // 2 >= y_min)
y_ub = y_dir_max

print(sum(fire_probe(x_dir, y_dir) for x_dir in range(x_lb, x_ub + 1) for y_dir in range(y_lb, y_ub + 1)))