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

# Keep track of the biggest three basin sizes
basins = [0, 0, 0]

while len(undiscovered) > 0:
    x, y = undiscovered.pop()
    value = field[y][x]

    # If any of the neighbours is lower or equal, discard the point.
    if x > 0 and value >= field[y][x - 1]: continue
    if x < x_max and value >= field[y][x + 1]: continue
    if y > 0 and value >= field[y - 1][x]: continue
    if y < y_max and value >= field[y + 1][x]: continue

    # None of the neighbors is lower. This must be a low point.
    
    def basinSize(x: int, y: int, basin: set) -> int:
        """
        Calculate the size of the basin, starting from the low point.
        :param x: x-coordinate of the current cell
        :param y: y-coordinate of the current cell
        :param basin: set of cells that are already discovered
        """
        if (x, y) in basin: return 0

        # We don't have to discover the current cell again
        if (x, y) in undiscovered: undiscovered.remove((x, y))

        # This is the boundary of the basin
        if field[y][x] == 9: return 0
        
        basin.add((x, y))
        size = 1

        # Spread to neighbors
        if x > 0: size += basinSize(x - 1, y, basin)
        if x < x_max: size += basinSize(x + 1, y, basin)
        if y > 0: size += basinSize(x, y - 1, basin)
        if y < y_max: size += basinSize(x, y + 1, basin)

        return size
    
    # Calculate the size of the basin.
    size = basinSize(x, y, set())

    # Check if the size is top 3 and insert if so
    for i in range(len(basins)):
        if size > basins[i]:
            basins.insert(i, size)
            
            # Remove the fourth element
            basins.pop(3)
            break

print(basins[0] * basins[1] * basins[2])