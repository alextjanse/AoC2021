bingoFuncs = __import__('4a') 

f = open('./input/4.txt')

numbers = list(map(int, f.readline().split(',')))

row = f.readline()

cards = []
numberCard = []

while row != '':
    if row == '\n':
        row = f.readline()
        continue

    numberCard.append(list(map(int, row.split())))

    if len(numberCard) == 5:
        markCard = [[False] * 5 for _ in range(5)]
        cards.append((numberCard.copy(), markCard))
        numberCard = []

    row = f.readline()

for number in numbers:
    # Copy the cards, so we have a version we can easily edit
    copy = cards.copy()
    
    # Take the indices in reverse order, so if we pop a bingo card,
    # the indices won't have been shifted.
    indices = list(enumerate(cards))
    indices.reverse()

    for index, (numberCard, markCard) in indices:
        for x, y in bingoFuncs.loop(5, 5):
            if numberCard[y][x] == number:
                markCard[y][x] = True

                if bingoFuncs.bingo(markCard, x, y):
                    copy.pop(index)

                    if len(cards) == 1:
                        # If this is the last bingo card, print the score
                        print(bingoFuncs.score(numberCard, markCard, number))
                        exit()

                break
    cards = copy