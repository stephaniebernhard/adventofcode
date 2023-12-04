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
    elif(char.isalpha()): #not needed if no letters in input
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

total_sum = 0

# check if symbol around number for each number
# wow, never seen code as ugly as this before...
for line_number in range(1,len(input)-1):
    line_sum_parts = 0
    line = input[line_number]
    numbers = all_numbers[line_number]
    last_pos = 0
    for number in all_numbers[line_number]:
        is_part_num = False
        number_length = len(number)
        pos=line.find(number, last_pos)
        last_pos = pos + len(number)
        #check lower left diagonal
        left_diag = input[line_number+1][pos-1]
        if (is_symbol(left_diag)):
            is_part_num = True
        #check lower middle
        for i in range(number_length):
            below = input[line_number+1][pos+i]
            if(is_symbol(below)):
                is_part_num = True
        #check lower right diagonal
        right_diag = input[line_number+1][pos+number_length]
        if(is_symbol(right_diag)):
            is_part_num = True
        #check front
        front = input[line_number][pos-1]
        if(is_symbol(front)):
            is_part_num = True
        #check back
        back = input[line_number][pos+number_length]
        if(is_symbol(back)):
            is_part_num = True
        #check higher left diag
        left_diag_up = input[line_number-1][pos-1]
        if (is_symbol(left_diag_up)):
            is_part_num = True
        #check higher middle
        for i in range(number_length):
            upper = input[line_number-1][pos+i]
            if(is_symbol(upper)):
                is_part_num = True
        #check higher right
        right_diag_up = input[line_number-1][pos+number_length]
        if(is_symbol(right_diag_up)):
            is_part_num = True
        if(is_part_num):
            line_sum_parts = line_sum_parts + int(number) 
    total_sum = total_sum + line_sum_parts

print(total_sum)
