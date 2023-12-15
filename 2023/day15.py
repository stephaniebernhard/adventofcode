from helpers import read_cwd

cwd = read_cwd()
            
def import_input(filename):
    my_list = []
    file_path = cwd+filename
    with open(file_path,"r") as f:
        for line in f:
            my_list= line.rstrip('\n').split(',')
    return my_list

input = import_input("day15.txt")

def my_hash(string):
    curr = 0
    for char in string:
        ascii_code = ord(char)
        curr = curr + ascii_code
        curr = curr*17
        curr = curr % 256
    return curr

total_sum = 0

for el in input:
    total_sum = total_sum + my_hash(el)

print(total_sum)