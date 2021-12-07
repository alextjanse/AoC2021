f = open('./input/1.txt')

line = f.readline()
i = int(line)
line = f.readline()

counter = 0

while line != '':
    j = int(line)

    if j > i:
        counter += 1

    i = j
    
    line = f.readline()

print(counter)