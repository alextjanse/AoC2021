###############
print('part 1')
###############

x = 0
y = 0

for line in open('./input/2.txt'):
    command, amount = line.split()
    i = int(amount)

    if command == 'forward':x += i
    elif command == 'down': y += i
    elif command == 'up': y -= i

print(x * y)

###############
print('part 2')
###############

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

print(x * y)