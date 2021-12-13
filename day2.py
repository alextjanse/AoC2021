################################
#            PART 1            #
################################

x = 0
y = 0

for line in open('./input/2.txt'):
    command, amount = line.split()
    i = int(amount)

    if command == 'forward':x += i
    elif command == 'down': y += i
    elif command == 'up': y -= i

print('part 1: {0}'.format(x * y))

################################
#            PART 2            #
################################

x = 0
y = 0
aim = 0

for line in open('./input/2.txt'):
    command, amount = line.split()
    i = int(amount)

    if command == 'forward':
        x += i
        y += aim * i
    elif command == 'up': aim -= i
    elif command == 'down': aim += i

print('part 2: {0}'.format(x * y))