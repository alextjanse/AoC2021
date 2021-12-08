from typing import Counter

f = open('./input/8.txt')

line = f.readline()

count = 0

# List of sets, so we can later easily check for set equality
original_patterns = [
    set('ABCEFG'),  # segments of zero
    set('CF'),      # segments of one
    set('ACDEG'),   # segments of two
    set('ACDFG'),   # segments of three
    set('BCDF'),    # segments of four
    set('ABDFG'),   # segments of five
    set('ABDEFG'),  # segments of six
    set('ACF'),     # segments of seven
    set('ABCDEFG'), # segments of eight
    set('ABCDFG'),  # segments of nine
]

while line != '':
    signal_patterns, output_value = list(map(lambda s: s.split(), line.split('|')))

    signal_patterns.sort(key=lambda s: len(s))

    # Dictionary with the maps from wires to original segment
    wire_maps = {}
    
    # Get maps to B, E and F by frequency
    frequency = Counter()
    for signal in signal_patterns:
        for wire in signal:
            frequency[wire] += 1

    for wire in frequency:
        if frequency[wire] == 4:
            wire_maps[wire] = 'E'
        elif frequency[wire] == 6:
            wire_maps[wire] = 'B'
        elif frequency[wire] == 9:
            wire_maps[wire] = 'F'

    # Get C by finding the signal for one
    for wire in signal_patterns[0]:
        if wire in wire_maps: continue
        wire_maps[wire] = 'C'
        break

    # Get A by finding the signal for seven
    for wire in signal_patterns[1]:
        if wire in wire_maps: continue
        wire_maps[wire] = 'A'
        break

    # Get D by finding the signal for four
    for wire in signal_patterns[2]:
        if wire in wire_maps: continue
        wire_maps[wire] = 'D'
        break

    # Get G by finding the last unassigned wire
    for wire in 'abcdefg':
        if wire in wire_maps: continue
        wire_maps[wire] = 'G'
        break

    # Calculate the output value
    value = 0
    for digit in output_value:
        # Map the output signal to the original segments
        pattern = set(map(lambda wire: wire_maps[wire], digit))

        # Check with each digit pattern if the sets match
        for i, original_pattern in enumerate(original_patterns):
            if pattern == original_pattern:
                value = 10 * value + i
                break

    count += value

    line = f.readline()

print(count)