f = open('./input/8.txt')

line = f.readline()

count = 0

while line != '':
    output_value = line.split('|')[1].split()

    for value in output_value:
        if len(value) in [2, 3, 4, 7]:
            count += 1

    line = f.readline()

print(count)