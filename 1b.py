f = open('./input/1.txt')

numbers = []

line = f.readline()

while line != '':
    i = int(line)

    numbers.append(i)

    line = f.readline()

counter = 0

"""
The problem tries to push you to a difficult solution, where you
would store seperate triplets, but this solution works much faster.
Summing these things up is O(1), so no need for difficult scanning.
"""
for i in range(len(numbers) - 3):
    if numbers[i] + numbers[i + 1] + numbers[i + 2] < numbers[i + 1] + numbers[i + 2] + numbers[i + 3]:
        counter += 1

print(counter)
