f = open('./input/3.txt')

numbers = []

line = f.readline()
bits = len(line) - 1

while line != '':
    numbers.append(line)
    
    line = f.readline()

def filterList(numberList, bit, most):
    count = 0

    for number in numberList:
        if number[bit] == '1': count += 1

    oneIsMost = count >= len(numberList) / 2

    value = '1' if (most and oneIsMost) or (not most and not oneIsMost) else '0'
    
    return list(filter(lambda number: number[bit] == value, numberList))

oxygenList = numbers.copy()
co2List = numbers.copy()

b = 0

while len(oxygenList) > 1:
    oxygenList = filterList(oxygenList, b, True)
    b += 1

b = 0

while len(co2List) > 1:
    co2List = filterList(co2List, b, False)
    b += 1

def bitsToInt(s):
    result = 0
    for b in range(bits):
        result *= 2
        result += int(s[b])
    return result

oxygen = bitsToInt(oxygenList[0])
co2 = bitsToInt(co2List[0])

print(oxygen * co2)