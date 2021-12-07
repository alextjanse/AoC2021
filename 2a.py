f = open('./input/2.txt')

x = 0
y = 0

line = f.readline()

while line != '':
    command, amount = line.split()
    i = int(amount)    

    if command == 'forward': x += i
    elif command == 'down': y += i
    elif command == 'up': y -= i

    line = f.readline()

print(x * y)