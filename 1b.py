f = open('./input/1.txt')

numbers = []

line = f.readline()

while line != '':
    i = int(line)

    numbers.append(i)

    line = f.readline()

counter = 0

for i in range(len(numbers) - 3):
    if numbers[i] + numbers[i + 1] + numbers[i + 2] < numbers[i + 1] + numbers[i + 2] + numbers[i + 3]:
        counter += 1

print(counter)