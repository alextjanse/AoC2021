f = open('./input/3.txt')

line = f.readline()

bits = len(line) - 1 # fuck \n

counters = [0] * bits
n = 0

while line != '':
    n += 1
    for i in range(bits):
        if line[i] == '1':
            counters[i] += 1

    line = f.readline()

gamma = 0

for i in range(bits):
    gamma *= 2
    if counters[i] > n / 2: gamma += 1

epsilon = 2**bits - 1 - gamma

print(gamma * epsilon)