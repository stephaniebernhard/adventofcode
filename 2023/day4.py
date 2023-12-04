from helpers import read_cwd

cwd = read_cwd()
            
def import_input(filename):
    my_list = []
    file_path = cwd+filename
    with open(file_path,"r") as f:
        for line in f:
            my_list.append(line.rstrip('\n')) 
    return my_list

input = import_input("day4.txt")

def format_input():
    arr = []
    for line in input:
        card_and_numbers = line.split(":")
        winning =  [int(s) for s in card_and_numbers[1].split("|")[0].split() if s.isdigit()] 
        numbers = [int(s) for s in card_and_numbers[1].split("|")[1].split() if s.isdigit()] 
        arr.append([winning, numbers])
    return arr

cards = format_input()
total_sum = 0

for card in cards: 
    count = 0
    for number in card[0]:
        if number in card[1]:
            count = count + 1
    if count>0:
        score = 2**(count-1)
        total_sum = total_sum + score

print(total_sum)
        