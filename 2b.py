f = open('./input/2.txt')

x = 0
y = 0
aim = 0

line = f.readline()

while line != '':
    command, amount = line.split()
    i = int(amount)    

    if command == 'forward':
        x += i
        y += aim * i
    elif command == 'up': aim -= i
    elif command == 'down': aim += i

    line = f.readline()

print(x * y)