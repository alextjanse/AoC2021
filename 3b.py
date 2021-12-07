from typing import List

f = open('./input/3.txt')

bit_strings = []

bit_string = f.readline()
bits = len(bit_string) - 1 # again, fuck \n

while bit_string != '':
    bit_strings.append(bit_string)
    
    bit_string = f.readline()

def filterList(bit_strings: List[str], bit_position: int, most: bool) -> List[str]:
    """
    :param bit_strings: the list of bits strings
    :param bit_position: the position of the bit that needs to be counted
    :param most: whether we are looking for the most or least common bit
    """
    count = 0

    for bit_string in bit_strings:
        if bit_string[bit_position] == '1': count += 1

    oneIsMost = count >= len(bit_strings) / 2

    value = '1' if (most and oneIsMost) or (not most and not oneIsMost) else '0'
    
    return list(filter(lambda bit_string: bit_string[bit_position] == value, bit_strings))

    # end function

# Start with looking for the oxygen level
oxygenList = bit_strings.copy()
bit_position = 0

while len(oxygenList) > 1:
    # while there are still items in the list, keep filtering
    oxygenList = filterList(oxygenList, bit_position, True)
    bit_position += 1

# Next, the co2 level
co2List = bit_strings.copy()
bit_position = 0

while len(co2List) > 1:
    co2List = filterList(co2List, bit_position, False)
    bit_position += 1

# Convert the single left bit string to their numbers
oxygen = int(oxygenList[0], 2)
co2 = int(co2List[0], 2)

print(oxygen * co2)