from collections import Counter

SORT_ORDER = {"A": 0,
              "K": 1,
              "Q": 2,
              "J": 3,
              "T": 4,
              "9": 5,
              "8": 6,
              "7": 7,
              "6": 8,
              "5": 9,
              "4": 10,
              "3": 11,
              "2": 12
            }

with open("./D$ay7/Day7_Input.txt",'r', encoding="utf-8") as file:
    file_parse = file.read().split('\n')

# hands = {}

five_of_kind = {}
four_of_kind = {}
full_house = {}
three_of_kind = {}
two_pair = {}
one_pair = {}
high_card = {}

for line in file_parse:
    hand, bid = line.split(' ')
    # hands[hand] = bid
    scored_hand = Counter(hand)

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

    # five of a kind
    else:
        five_of_kind[hand] = bid


print("Num of five_of_kind: " + str(len(five_of_kind)))
print("Num of four_of_kind: " + str(len(four_of_kind)))
print("Num of full_house: " + str(len(full_house)))
print("Num of three_of_kind: " + str(len(three_of_kind)))
print("Num of two_pair: " + str(len(two_pair)))
print("Num of one_pair: " + str(len(one_pair)))
print("Num of high_card: " + str(len(high_card)))
