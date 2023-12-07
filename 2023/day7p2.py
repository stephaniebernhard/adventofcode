from helpers import read_cwd
from functools import cmp_to_key

cwd = read_cwd()
            
def import_input(filename):
    my_list = []
    file_path = cwd+filename
    with open(file_path,"r") as f:
        for line in f:
            my_list.append(line.rstrip('\n')) 
    return my_list

input = import_input("day7.txt")
hands = []
bids = []

for el in input:
    hands.append(el.split(" ")[0])
    bids.append(el.split(" ")[1])

bids_map = {}

for i in range(len(hands)):
    bids_map[hands[i]]=bids[i]

def get_hand_map(hand):
    map = {}
    for char in hand:
        if char in map:
            map[char] = map[char]+1
        else:
            map[char] = 1
    return map


def get_type(map):
    type = 0
    jokers = 0
    if 'J' in map.keys():
        jokers = map['J']
        map['J']=0
    if jokers==0:
        # five of a kind
        if(5 in map.values()):
            type = 6
        # four of a kind
        elif(4 in map.values()):
            type = 5
        # full house
        elif(3 in map.values() and 2 in map.values()):
            type = 4
        # three of a kind
        elif(3 in map.values()):
            type = 3
        elif(2 in map.values()):
            count = 0
            for value in map.values():
                if value==2:
                    count = count + 1
            # two pairs
            if count >=2:
                type = 2
            # one pair
            else:
                type = 1
    elif jokers == 1:
        if(4 in map.values()):
            type = 6
        elif(3 in map.values()):
            type = 5
        elif(2 in map.values()):
            count = 0
            for value in map.values():
                if value==2:
                    count = count + 1
            # two pairs
            if count >=2:
                type = 4
            else:
                type = 3
        else:
            type = 1
    elif jokers == 2:
        if(3 in map.values()):
            type = 6
        elif(2 in map.values()):
            type = 5
        else:
            type = 3
    elif jokers == 3:
        if(2 in map.values()):
            type = 6
        else:
            type = 5
    elif jokers >= 4:
        type = 6
    map['J']=jokers
    return type

hand_type_map = {}

for hand in hands:
    hand_type_map[hand] = get_type(get_hand_map(hand))

type_arr = [0,1,2,3,4,5,6]

order = ['J','2','3','4','5','6','7','8','9','T','J','Q','K','A']

# use sort function with key and write compare function
def compare(hand1, hand2):
    winning_hand = ""
    for i in range(5):
        if(hand1==hand2):
            winning_hand = 0
            break
        if(order.index(hand1[i]) > order.index(hand2[i])):
            winning_hand = 1
            break
        if(order.index(hand1[i]) < order.index(hand2[i])):
            winning_hand = -1
            break
    return winning_hand

sorted_hand_list = []

for type in type_arr:
    hands = [k for k, v in hand_type_map.items() if v==type]
    sorted_hands = sorted(hands, key=cmp_to_key(compare))
    for hand in sorted_hands:
        sorted_hand_list.append(hand)

total_winnings = 0
for i in range(len(sorted_hand_list)):
    total_winnings = total_winnings + (i+1)*int(bids_map[sorted_hand_list[i]])

print(total_winnings)