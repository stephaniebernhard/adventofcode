def read_cwd():
    path = ""
    with open('path.txt', "r") as f:
        for line in f:
            path = line.rstrip('\n')
    return path

cwd = read_cwd()
            
def import_input():
    my_list = []
    file_path = cwd+"day3.txt"
    with open(file_path,"r") as f:
        for line in f:
            my_list.append("."+line.rstrip('\n')+".") 
    return my_list

input = import_input()
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
print(input)


def is_symbol(char):
    symbol = True
    if(char.isdigit()):
        symbol = False
    elif(char=="."):
        symbol = False
    elif(char.isalpha()): #not needed if no letters in input
        symbol = False
    return symbol


#todo handle first and last line separately

#todo iterate through all lines in between
def get_all_numbers(input):
    arr = []
    for line_number in range(number_of_lines):
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

for line_number in range(number_of_lines):
    line_sum_parts = 0
    line = input[line_number]
    numbers = all_numbers[line_number]
    if(line_number==0):
        print("line1")
        for number in all_numbers[0]:
            is_part_num = False
            number_length = len(number)
            pos=line.find(number)
            #check left diagonal
            left_diag = input[line_number+1][pos-1]
            if (is_symbol(left_diag)):
                is_part_num = True
            #check middle
            for i in range(number_length):
                below = input[line_number+1][pos+i]
                if(is_symbol(below)):
                    is_part_num = True
            #check right diagonal
            right_diag = input[line_number+1][pos+number_length]
            if(is_symbol(right_diag)):
                is_part_num = True
            if (is_part_num):
                line_sum_parts = line_sum_parts + int(number)      
        print("sum of part nums: "+ str(line_sum_parts)) 
    elif(line_number==(number_of_lines)):
        print("line"+str(line_number+1))
    else:
        print("line"+str(line_number+1))
    