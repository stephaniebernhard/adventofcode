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
            my_list.append(line.rstrip('\n')) 
    return my_list

input = import_input()
line_length = len(input[0])
number_of_lines = len(input)

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
            read_number=False
            character = line[pos]
            if(character.isdigit()):
                read_number = True
                current_number = current_number + character
            else:
                if(current_number!=""):
                    number_array.append(current_number)
                read_number = False
                current_number = ""
            if(pos==line_length-1 and current_number!=""):
                    number_array.append(current_number)
        arr.append(number_array)
    return arr

all_numbers = get_all_numbers(input)
print(all_numbers)

