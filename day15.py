from queue import PriorityQueue
from math import sqrt

original_risk_levels = list(map(lambda row: list(map(int, row)), open('./input/15.txt').read().split('\n')))

###############
print('part 1')
###############

"""
I used Uniform-Cost Search.
"""

risk_levels = original_risk_levels
x_max, y_max = len(risk_levels[0]), len(risk_levels)

queue = PriorityQueue()
queue.put((0, (0, 0)))

distances = {}

distances[(0, 0)] = 0

visited = set()

while not queue.empty():
    distance, node = queue.get()
    x, y = node

    if node in visited: continue
    
    visited.add(node)

    distances[node] = distance

    if node == (x_max - 1, y_max - 1):
        break

    if x > 0: queue.put((distance + risk_levels[y][x - 1], (x - 1, y)))
    if y > 0: queue.put((distance + risk_levels[y - 1][x], (x, y - 1)))

    if x < x_max - 1: queue.put((distance + risk_levels[y][x + 1], (x + 1, y)))
    if y < y_max - 1: queue.put((distance + risk_levels[y + 1][x], (x, y + 1)))
    
print(distances[(x_max - 1, y_max - 1)])

###############
print('part 2')
###############

risk_levels = []

for j in range(5):
    for row in original_risk_levels:
        line = []
        for i in range(5):
            for cell in row:
                value = (cell + i + j - 1) % 9 + 1
                line.append(value)
        risk_levels.append(line)

x_max, y_max = len(risk_levels[0]), len(risk_levels)

"""
Add heuristics (Euclidian distance) to make it A*
"""

queue = PriorityQueue()
queue.put((0, 0, (0, 0)))

distances = {}

distances[(0, 0)] = 0

visited = set()

def heuristic(node):
    x, y = node
    return sqrt((x_max - x)**2 + (y_max - y)**2)

while not queue.empty():
    _, distance, node = queue.get()
    x, y = node

    if node in visited: continue
    
    visited.add(node)

    distances[node] = distance

    if node == (x_max - 1, y_max - 1):
        break

    if x > 0:
        n = (x - 1, y)
        d = distance + risk_levels[y][x - 1]
        h = heuristic(n) + d
        queue.put((h, d, n))
        
    if y > 0:
        n = (x, y - 1)
        d = distance + risk_levels[y - 1][x]
        h = heuristic(n) + d
        queue.put((h, d, n))

    if x < x_max - 1:
        n = (x + 1, y)
        d = distance + risk_levels[y][x + 1]
        h = heuristic(n) + d
        queue.put((h, d, n))

    if y < y_max - 1:
        n = (x, y + 1)
        d = distance + risk_levels[y + 1][x]
        h = heuristic(n) + d
        queue.put((h, d, n))

print(distances[(x_max - 1, y_max - 1)])