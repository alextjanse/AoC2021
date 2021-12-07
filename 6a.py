f = open('./input/6.txt')

fishes = [0] * 9

for i in map(int, f.readline().split(',')):
    fishes[i] += 1

days = 80

"""
I realized that you can just swap the cycles around. I first cycled
over the 7-day birthing cycle, but then you would get

    fishes[(day + 9) % 7] = fishes[(day + 2) % 7]

which fails, because the growth time would be only 2 days this way.
I circumvented this problem by making a second 7-cycle list, storing
the offsprings and introducing the offsprings into the "adult pool"
at the beginning of the day.

This new solution is much more elegant. You can just cycle over the
growth cycle; the current day fishes "lay their eggs", so that they
are fully grown in the next cycle. Meanwhile, we add the fishes to
(day + 7) % 9, because on that day they will lay eggs again.
"""

for day in range(days): fishes[(day + 7) % 9] += fishes[day % 9]

print(sum(fishes))