import utils

field = [list(map(int, line.rstrip())) for line in open('./input/11.txt')]

def flash(x: int, y: int, flashed: set) -> int:
    # Out of bounds
    if x < 0 or x == 10 or y < 0 or y == 10: return 0

    # Already flashed this iteration
    if (x, y) in flashed: return 0

    field[y][x] += 1

    if field[y][x] == 10:
        # Flash!
        field[y][x] = 0
        flashed.add((x, y))

        flashes = 1
        for y_offset in range(-1, 2):
            for x_offset in range(-1, 2):
                flashes += flash(x + x_offset, y + y_offset, flashed)

        return flashes
    
    return 0

iterations = 0

while True:
    iterations += 1

    flashed = set()

    for i, j in utils.loop(10, 10): flash(i, j, flashed)

    if len(flashed) == 100: break

print(iterations)
