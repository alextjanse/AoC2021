import queue

f = open('./input/13.txt')

line = f.readline().rstrip()

# parse points
points = []

while line != '':
    x, y = map(int, line.split(','))

    points.append((x,y))

    line = f.readline().rstrip()

# parse folds
line = f.readline().rstrip()

folds = []

while line != '':
    axis, value = line[11:].split('=')
    value = int(value)
    folds.append((axis, value))

    line = f.readline().rstrip()

###############
print('part 1')
###############

for axis, value in folds[:1]:
    new_points = set()
    for x, y in points:
        if axis == 'y':
            y = value - abs(y - value)
        elif axis == 'x':
            x = value - abs(x - value)
        new_points.add((x,y))
    points = list(new_points)

print(len(points))

###############
print('part 2')
###############

x_max, y_max = 0,0

for axis, value in folds[1:]:
    new_points = set()

    # reset the bounds, we only want the values after the last fold
    x_max, y_max = 0,0

    for x, y in points:
        if axis == 'y':
            y = value - abs(y - value)
        elif axis == 'x':
            x = value - abs(x - value)
        new_points.add((x,y))

        x_max, y_max = max(x_max, x), max(y_max, y)

    points = list(new_points)

bitmap = [[' '] * (x_max + 1) for _ in range(y_max + 1)]

for x,y in points: bitmap[y][x] = '#'

for row in bitmap: print(''.join(row))