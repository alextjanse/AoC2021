f = open('./input/4.txt')

numbers = list(map(int, f.readline().split(',')))

line = f.readline()

cards = []
numberCard = []

while line != '':
    if line == '\n':
        line = f.readline()
        continue

    numberCard.append(list(map(int, line.split())))

    if len(numberCard) == 5:
        markCard = [[False] * 5 for _ in range(5)]
        cards.append((numberCard.copy(), markCard))
        numberCard = []

    line = f.readline()

for number in numbers:
    for (numberCard, markCard) in cards:
        for y in range(5):
            for x in range(5):
                if numberCard[y][x] == number:
                    markCard[y][x] = True

                    horizontalCount = 0
                    verticalCount = 0

                    for i in range(5):
                        if markCard[y][i]: horizontalCount += 1
                        if markCard[i][x]: verticalCount += 1

                    if horizontalCount == 5 or verticalCount == 5:
                        unmarkedSum = 0
                        for j in range(5):
                            for i in range(5):
                                if not markCard[j][i]: unmarkedSum += numberCard[j][i]
                        
                        print(unmarkedSum * number)
                        exit()