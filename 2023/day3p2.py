from helpers import read_cwd

cwd = read_cwd()
            
def import_input(filename):
    my_list = []
    file_path = cwd+filename
    with open(file_path,"r") as f:
        for line in f:
            my_list.append("."+line.rstrip('\n')+".") 
    return my_list

input = import_input("day3.txt")
line_length = len(input[0])
number_of_lines = len(input)

# magic to prevent index out of range
def manipulate_input(input):
    added_string = ""
    for i in range(line_length):
        added_string = added_string+"."
    new_input = [added_string]
    for line in input:
        new_input.append(line)
    new_input.append(added_string)
    return new_input

input = manipulate_input(input)

def is_symbol(char):
    symbol = True
    if(char.isdigit()):
        symbol = False
    elif(char=="."):
        symbol = False
    return symbol

# get all numbers from a line
def get_all_numbers(input):
    arr = []
    for line_number in range(len(input)):
        line = input[line_number]
        current_number = ""
        number_array = []
        for pos in range(line_length):
            character = line[pos]
            if(character.isdigit()):
                current_number = current_number + character
            else:
                if(current_number!=""):
                    number_array.append(current_number)
                current_number = ""
            if(pos==line_length-1 and current_number!=""):
                    number_array.append(current_number)
        arr.append(number_array)
    return arr

all_numbers = get_all_numbers(input)

number_data = []
gear_indices = []

def findall(p, s):
    i = s.find(p)
    while i != -1:
        yield i
        i = s.find(p, i+1)

#get all gear indices and part number start and end indices
for line_number in range(1,len(input)-1):
    line_sum_parts = 0
    line = input[line_number]
    numbers = all_numbers[line_number]
    last_pos = 0
    row = []
    for number in all_numbers[line_number]:
        is_part_num = False
        number_length = len(number)
        pos=line.find(number, last_pos)
        last_pos = pos + len(number)
        row.append([number, pos, pos+number_length])
    number_data.append(row)
    gear_indices.append([i for i in findall('*', input[line_number])])

total_sum = 0


def check_for_partnums(gear, partnum):
    return gear-1 in range(partnum[1],partnum[2]) or gear in range(partnum[1],partnum[2]) or gear+1 in range(partnum[1],partnum[2])

for line_number in range(len(number_data)):
    gears = gear_indices[line_number]
    # get number of partnums around each gear
    for gear in gears:
        adj_partnums = set()
        for partnum in number_data[line_number-1]:
            if(check_for_partnums(gear, partnum)):
                adj_partnums.add(partnum[0])
        for partnum in number_data[line_number]:
            if(check_for_partnums(gear, partnum)):
                adj_partnums.add(partnum[0])
        for partnum in number_data[line_number+1]:
            if(check_for_partnums(gear, partnum)):
                adj_partnums.add(partnum[0])
        # only count if 2 adjacent partnums
        if(len(adj_partnums)==2):
            product = 1
            for el in adj_partnums:
                product = product * int(el)
            total_sum = total_sum + product

print(total_sum)