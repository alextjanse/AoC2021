numbers = [int(line) for line in open('./input/1.txt')]

################################
#            PART 1            #
################################

counter = 0

for i in range(len(numbers) - 1):
    if numbers[i] < numbers[i + 1]: counter += 1

print('part 1: {0}'.format(counter))

################################
#            PART 2            #
################################

counter = 0

for i in range(len(numbers) - 3):
    if sum(numbers[i: i + 3]) < sum(numbers[i + 1: i + 4]): counter += 1

print('part 2: {0}'.format(counter))