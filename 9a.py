f = open('./input/9.txt')

line = f.readline()

field = []

# set of points we haven't discovered yet
undiscovered = set()

y = 0
while line != '':
    row = []
    x = 0
    for char in line:
        if char == '\n': continue
        row.append(int(char))
        undiscovered.add((x, y))
        x += 1
    
    field.append(row)

    y += 1
    line = f.readline()

# Set the x_max and y_max (for boundary check)
x_max, y_max = len(field[0]) - 1, len(field) - 1

result = 0

while len(undiscovered) > 0:
    x, y = undiscovered.pop()
    value = field[y][x]

    # If any of the neighbours is lower or equal, discard the point.
    if x > 0 and value >= field[y][x - 1]: continue
    if x < x_max and value >= field[y][x + 1]: continue
    if y > 0 and value >= field[y - 1][x]: continue
    if y < y_max and value >= field[y + 1][x]: continue

    # None of the neighbors is lower. This must be a low point.
    result += 1 + value

print(result)