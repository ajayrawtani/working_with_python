#!/usr/bin/env python3

from random import shuffle


def generate_deck():
    """ Create a deck, shuffle and split it between two players """
    deck = []
    for face in range(2, 15):
        for suit in 'DHSC':
            deck.append((face, suit))
    shuffle(deck)

    return deck[:26], deck[26:]


def take_cards(winner, a, b, common):
    """Re-arrange cards to winners or common pool"""
    if winner == 'a':
        a.append(a[0])
        a.append(b[0])
        a.pop(0)
        b.pop(0)
        if len(common) != 0:
            a.extend(common)
            common.clear()
        return a, b, common
    elif winner == 'b':
        b.append(b[0])
        b.append(a[0])
        b.pop(0)
        a.pop(0)
        if len(common) != 0:
            b.extend(common)
            common.clear()
        return a, b, common
    else:
        common.append(a[0])
        common.append(b[0])
        a.pop(0)
        b.pop(0)
        return a, b, common


def play(a, b):
    """Determine the higher of the two hands"""
    if a[0] > b[0]:
        return 'a'
    elif b[0] > a[0]:
        return 'b'
    else:
        return 'None'


def main():
    n = int(input("Enter the number of simulations: "))

    TotalSum = 0

    for i in range(n):
        a, b = generate_deck()  # Calling function to generate decks
        common = []  # create a common deck
        plays = 0  # Initiate the plays count to count rounds played

        # Loop until both players have cards in their hand at the end of each round
        while len(a) > 0 and len(b) > 0:
            winner = play(a[0], b[0])  # call function to determine the winner, returns a string
            a, b, common = take_cards(winner, a, b,
                                      common)  # call function to pass cards to winner or place in common pool

            # Reshuffle the common pool if there are cards in it, to avoid infinite loop
            if len(common) != 0:
                shuffle(common)

            # print(winner)
            # print(common)

            plays += 1

        print(f'It took {plays} plays to finish game number {i + 1}')

        TotalSum += plays

    print(f'The average cards to a game in {n} games is {round(TotalSum/n)} (rounded to the nearest integer)')


main()
