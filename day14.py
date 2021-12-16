from typing import Counter


f = open('./input/14.txt')

original_polymer = f.readline().rstrip()

f.readline() # skip empty line

maps = dict()

line = f.readline().rstrip()

while line != '':
    a, b = line.split(' -> ')
    maps[a] = b

    line = f.readline().rstrip()

###############
print('part 1')
###############

polymer = original_polymer

letters = Counter()

for c in polymer:
    letters[c] += 1

def pair_insertion(a, steps):
    if steps == 0: return

    insertion = maps[a]
    letters[insertion] += 1

    a = a[:1] + insertion + a[1:]

    pair_insertion(a[:2], steps - 1)
    pair_insertion(a[1:], steps - 1)

for i in range(len(polymer) - 1):
    pair_insertion(polymer[i: i + 2], 10)

min_letter = min(letters, key=letters.get)
min_value = letters[min_letter]

max_letter = max(letters, key=letters.get)
max_value = letters[max_letter]

print('min: {}, {}'.format(min_letter, min_value))
print('max: {}, {}'.format(max_letter, max_value))
print('{} - {} = {}'.format(max_value, min_value, max_value - min_value))


###############
print('part 2')
###############

polymer = original_polymer

combinations = Counter()

for i in range(len(polymer) - 1):
    combinations[polymer[i: i + 2]] += 1

letters = Counter()

for c in polymer:
    letters[c] += 1

for step in range(40):
    new_combinations = Counter()

    for a, count in combinations.items():
        insertion = maps[a]
        letters[insertion] += count

        b = a[:1] + insertion + a[1:]
        
        new_combinations[b[:2]] += count
        new_combinations[b[1:]] += count

    combinations = new_combinations

min_letter = min(letters, key=letters.get)
min_value = letters[min_letter]

max_letter = max(letters, key=letters.get)
max_value = letters[max_letter]

print('min: {}, {}'.format(min_letter, min_value))
print('max: {}, {}'.format(max_letter, max_value))
print('{} - {} = {}'.format(max_value, min_value, max_value - min_value))