def new_stack(cards):
    return cards[::-1]


def cut_n(cards, n):
    if n > 0:
        new_cards = cards[n:] + cards[:n]
    else:
        new_cards = cards[n:] + cards[:n]
    return new_cards


def increment_n(cards, n):
    new_cards = [None] * len(cards)
    i = 0
    for card in cards:
        new_cards[i] = card
        i = (i + n) % len(cards)
    return new_cards


my_cards = list(range(10007))
lineList = [line.rstrip('\n') for line in open('inputs/day22.txt')]
for line in lineList:
    commands = line.split()
    if commands[1] == 'into':
        my_cards = new_stack(my_cards)
    if commands[1] == 'with':
        my_cards = increment_n(my_cards, int(commands[-1]))
    if commands[0] == 'cut':
        my_cards = cut_n(my_cards, int(commands[-1]))

print(my_cards.index(2019))
