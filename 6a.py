f = open('./input/6.txt')

fishes = [0] * 7

for i in map(int, f.readline().split(',')):
    fishes[i] += 1

days = 80

babies = [0] * 9

for day in range(days):    
    fishes[day % 7] += babies[day % 9]
    babies[day % 9] = fishes[day % 7]

print(sum(fishes) + sum(babies))