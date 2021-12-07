from typing import Counter

f = open('./input/5.txt')

line = f.readline()

points = []

while line != '':
    p1, p2 = line.split(' -> ')
    
    x1, y1 = list(map(int, p1.split(',')))
    x2, y2 = list(map(int, p2.split(',')))

    points.append((x1, y1, x2, y2))

    line = f.readline()

overlaps = Counter()
count = 0

for x1, y1, x2, y2 in points:
    x_start = x1
    y_start = y1
    x_dir = (x2 - x1) // max(abs(x2 - x1), 1)
    y_dir = (y2 - y1) // max(abs(y2 - y1), 1)
    length = max(abs(x2 - x1), abs(y2 - y1)) + 1

    # Only difference is that we don't filter out diagonal lines anymore.

    for j in range(length):
        x = x_start + j * x_dir
        y = y_start + j * y_dir

        overlaps[(x, y)] += 1
        if overlaps[(x, y)] == 2: count += 1
        
print(count)