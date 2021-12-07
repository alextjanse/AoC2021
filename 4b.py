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

def loop(xrange, yrange):
    for y in range(yrange):
        for x in range(xrange):
            yield x, y

def bingo(numberCard: list, markCard: list, x: int, y: int) -> bool:
    horizontalCount = 0
    verticalCount = 0
    for i in range(5):
        if markCard[y][i]: horizontalCount += 1
        if markCard[i][x]: verticalCount += 1
    return horizontalCount == 5 or verticalCount == 5

def score(numberCard: list, markCard: list, number: int) -> int:
    unmarkedSum = 0
    for y in range(5):
        for x in range(5):
            if not markCard[y][x]: unmarkedSum += numberCard[y][x]
    return unmarkedSum * number

for number in numbers:
    copy = cards.copy()
    
    indices = list(enumerate(cards))
    indices.reverse()

    for index, (numberCard, markCard) in indices:
        for x, y in loop(5, 5):
            if numberCard[y][x] == number:
                markCard[y][x] = True

                if bingo(numberCard, markCard, x, y):
                    copy.pop(index)

                    if len(cards) == 1:
                        print(score(numberCard, markCard, number))
                        exit()

                break
    cards = copy