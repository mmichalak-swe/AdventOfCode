from collections import Counter

SORT_ORDER_ASC = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
SORT_ORDER_DES = SORT_ORDER_ASC[::-1]

with open("./Day7/Day7_Input.txt",'r', encoding="utf-8") as file:
    file_parse = file.read().split('\n')

five_of_kind = {}
four_of_kind = {}
full_house = {}
three_of_kind = {}
two_pair = {}
one_pair = {}
high_card = {}

for line in file_parse:
    hand, bid = line.split(' ')
    scored_hand = Counter(hand)

    # five of a kind right away, no J
    if len(scored_hand) == 1:
        five_of_kind[hand] = bid
    else:
        if 'J' in scored_hand.keys():
            j_to_add = scored_hand['J']
            del scored_hand['J']
            scored_hand = dict(sorted(scored_hand.items(), key=lambda x: (x[1], [SORT_ORDER_ASC.index(c) for c in x[0]])))
            last_key, last_val = _, scored_hand[last_key] = scored_hand.popitem()
            scored_hand[last_key] = last_val + j_to_add

    # high card
    if len(scored_hand) == 5:
        high_card[hand] = bid

    # one pair
    elif len(scored_hand) == 4:
        one_pair[hand] = bid

    # two pair, three of a kind
    elif len(scored_hand) == 3:
        if 3 not in scored_hand.values():
            two_pair[hand] = bid
        else:
            three_of_kind[hand] = bid

    # full house, four of a kind
    elif len(scored_hand) == 2:
        if 4 not in scored_hand.values():
            full_house[hand] = bid
        else:
            four_of_kind[hand] = bid

    # five of a kind after J transform
    else:
        five_of_kind[hand] = bid


five_of_kind = dict(sorted(five_of_kind.items(), key=lambda x: [SORT_ORDER_ASC.index(c) for c in x[0]]))
four_of_kind = dict(sorted(four_of_kind.items(), key=lambda x: [SORT_ORDER_ASC.index(c) for c in x[0]]))
full_house = dict(sorted(full_house.items(), key=lambda x: [SORT_ORDER_ASC.index(c) for c in x[0]]))
three_of_kind = dict(sorted(three_of_kind.items(), key=lambda x: [SORT_ORDER_ASC.index(c) for c in x[0]]))
two_pair = dict(sorted(two_pair.items(), key=lambda x: [SORT_ORDER_ASC.index(c) for c in x[0]]))
one_pair = dict(sorted(one_pair.items(), key=lambda x: [SORT_ORDER_ASC.index(c) for c in x[0]]))
high_card = dict(sorted(high_card.items(), key=lambda x: [SORT_ORDER_ASC.index(c) for c in x[0]]))

ordered_hands = {**high_card, **one_pair, **two_pair, **three_of_kind, **full_house, **four_of_kind, **five_of_kind}

output = 0
multiplier = 1

for val in ordered_hands.values():
    output += int(val) * multiplier
    multiplier += 1

print(output)
