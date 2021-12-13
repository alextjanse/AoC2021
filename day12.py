from typing import List, DefaultDict, Tuple
from collections import defaultdict

nodes: DefaultDict[str, List[str]] = defaultdict(list)

for line in open('./input/12.txt'):
    v, w = line.rstrip().split('-')
    nodes[v].append(w)
    nodes[w].append(v)

################################
#            PART 1            #
################################

route_stack: List[List[str]] = []
route_stack.append(['start'])

route_counter = 0

while len(route_stack) > 0:
    route = route_stack.pop()

    last_node = route[-1]

    if last_node == 'end':
        route_counter += 1
        continue

    # route hasn't ended yet
    for neigbor in nodes[last_node]:
        if neigbor.islower() and neigbor in route:
            continue

        new_route = route + [neigbor]
        route_stack.append(new_route)

print('part 1: {0}'.format(route_counter))

################################
#            PART 2            #
################################

route_stack: Tuple[List[str], bool] = []
route_stack.append((['start'], False))

route_counter = 0

while len(route_stack) > 0:
    route, smallCaveVisitedTwice = route_stack.pop()

    last_node = route[-1]

    if last_node == 'end':
        route_counter += 1
        continue

    # route hasn't ended yet
    for neigbor in nodes[last_node]:
        if neigbor == 'start': continue

        new_route = route + [neigbor]
        new_smallCaveVisitedTwice = smallCaveVisitedTwice

        if neigbor.islower() and neigbor in route:
            if smallCaveVisitedTwice: continue
            else: new_smallCaveVisitedTwice = True

        route_stack.append((new_route, new_smallCaveVisitedTwice))

print('part 2: {0}'.format(route_counter))