from typing import List
import utils

def bingo(markCard: List[List[bool]], x: int, y: int) -> bool:
    """
    Checks if the current mark card has a bingo on it, given
    the row and column in which to look.
    :param x: the row in which to look.
    :param y: the column in which to look.
    """
    horizontalCount = 0
    verticalCount = 0
    for i in range(5):
        if markCard[y][i]: horizontalCount += 1
        if markCard[i][x]: verticalCount += 1
    return horizontalCount == 5 or verticalCount == 5

def score(numberCard: List[List[int]], markCard: List[List[bool]], number: int) -> int:
    """
    Calculate the score of the bingo card. I really wanted to do a Python one-liner.
    :param numberCard: the bingo card with the numbers.
    :param markCard: the bingo card with the marked off cells.
    :param number: the current called number.
    """
    return number * sum(map(lambda i: 0 if markCard[i[1]][i[0]] else numberCard[i[1]][i[0]], utils.loop(5, 5)))

if __name__== '__main__':
    # Damn, whole main block and all. It's almost like a real program!
    
    f = open('./input/4.txt')

    numbers = list(map(int, f.readline().split(',')))

    row = f.readline()

    cards = []
    numberCard = []

    while row != '':
        if row == '\n':
            row = f.readline()
            continue

        # Add the row to the number card
        numberCard.append(list(map(int, row.split())))

        if len(numberCard) == 5:
            # We've got 5 numbers, the card is complete

            # The mark card is where we keep track of the called numbers of this card
            markCard = [[False] * 5 for _ in range(5)]

            # We make a copy of the number card to prevent them all pointing to the same list
            cards.append((numberCard.copy(), markCard))
            numberCard = []

        row = f.readline()

    for number in numbers:
        # Call all the numbers one by one
        for (numberCard, markCard) in cards:
            # Check the number on every card
            for x,y in utils.loop(5, 5):
                if numberCard[y][x] == number:
                    # Check off the number
                    markCard[y][x] = True

                    if bingo(markCard, x, y):
                        # We got bingo! Calculate the score.
                        print(score(numberCard, markCard, number))
                        exit()