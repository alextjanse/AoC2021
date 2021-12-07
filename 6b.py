f = open('./input/6.txt')

fishes = [0] * 9

for i in map(int, f.readline().split(',')):
    fishes[i] += 1

days = 256

# Explanation in 6a.py
for day in range(days): fishes[(day + 7) % 9] += fishes[day % 9]

print(sum(fishes))