f = open('./input/6.txt')

fishes = [0] * 9

for i in map(int, f.readline().split(',')):
    fishes[i] += 1

days = 256

# Explanation in 6a.py
for t in range(days): fishes[(t + 7) % 9] += fishes[t % 9]

print(sum(fishes))