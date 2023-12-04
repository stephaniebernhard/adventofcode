from helpers import read_cwd
import re

cwd = read_cwd()
            
def import_input(filename):
    my_list = []
    file_path = cwd+filename
    with open(file_path,"r") as f:
        for line in f:
            my_list.append(line.rstrip('\n')) 
    return my_list

input = import_input("day3.txt")
line_length = len(input[0])

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

def findall(p, s):
    i = s.find(p)
    while i != -1:
        yield i
        i = s.find(p, i+1)

gear_indices = []

for line in input:
    gear_indices.append([i for i in findall('*', line)])

print(gear_indices)

#giving up for the moment