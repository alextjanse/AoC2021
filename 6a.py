f = open('./input/6.txt')

fishes = [0] * 9

for i in map(int, f.readline().split(',')):
    fishes[i] += 1

days = 80

"""
I realized that you can just swap the cycles around. I first cycled
over the 7-day birthing cycle, but then you would get something like
(t + 9) % 7, which is equivalent to (t + 2) % 7. This would mean
that you would encounter the fishes at t + 2 and you wouldn't be able
to easily distiguish between the mature fish and the younglings.
I circumvented this problem by making a seperate 9-cycle, storing
the younglings. At each day, i would join the younglings with the
adults: like having the fish mature in a seperate pool or something.
Then I would "take the eggs" of the mature fish and place them in the
empty maturing pool and store them away for 9 days.

This new solution is much more elegant. You can just cycle over the
growth cycle; the current day fishes "lay their eggs", so that they
are fully grown in the next cycle. Meanwhile, we add the fishes to
(day + 7) % 9, because on that day they will lay eggs again.
"""

for t in range(days): fishes[(t + 7) % 9] += fishes[t % 9]

print(sum(fishes))