from collections import Counter
import functools

ranks = [[] for i in range(7)]
replacements = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 1,
    'T': 10
}


def card_sort(a, b):
    card_a = replacements[a] if a in replacements else int(a)
    card_b = replacements[b] if b in replacements else int(b)
    if card_a > card_b:
        return 1
    elif card_b > card_a:
        return -1
    return 0


def hand_sort(a, b):
    for i in range(5):
        card_a = a[0][i]
        card_b = b[0][i]
        card_a = replacements[card_a] if card_a in replacements else int(card_a)
        card_b = replacements[card_b] if card_b in replacements else int(card_b)
        if card_a > card_b:
            return 1
        elif card_b > card_a:
            return -1
    return 0


for line in open('../input.txt'):
    hand, bid = line.strip().split(maxsplit=1)
    cards = Counter()
    sorted_hand = ''.join(sorted(hand, key=functools.cmp_to_key(card_sort), reverse=True))
    for card in sorted_hand:
        if card != 'J':
            cards.update({card: 1})

    if hand == 'JJJJJ':
        jokerfied_hand = 'AAAAA'
    elif 'J' in hand:
        jokerfied_hand = hand.replace('J', cards.most_common(1)[0][0])
    else:
        jokerfied_hand = hand

    jokerfied_cards = Counter()
    for card in jokerfied_hand:
        jokerfied_cards.update({card: 1})

    if len(jokerfied_cards) == 1:
        ranks[0].append((hand, bid))
    elif len(jokerfied_cards) == 5:
        ranks[6].append((hand, bid))
    elif 4 in jokerfied_cards.values():
        ranks[1].append((hand, bid))
    elif 3 in jokerfied_cards.values():
        if 2 in jokerfied_cards.values():
            ranks[2].append((hand, bid))
        else:
            ranks[3].append((hand, bid))
    elif 2 in jokerfied_cards.values():
        if jokerfied_cards.most_common(2)[1][1] == 2:
            ranks[4].append((hand, bid))
        else:
            ranks[5].append((hand, bid))
    else:
        ranks[6].append((hand, bid))

sorted_ranks = []
for rank in ranks:
    if len(rank) > 0:
        sorted_ranks.append(sorted(rank, key=functools.cmp_to_key(hand_sort), reverse=True))
sorted_hands = [hand for rank in sorted_ranks for hand in rank]
sorted_hands.reverse()

total_winnings = 0
for i, hand in enumerate(sorted_hands):
    total_winnings += (i + 1) * int(hand[1])

print(total_winnings)
