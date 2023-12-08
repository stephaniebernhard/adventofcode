import math
from functools import reduce
from helpers import read_cwd

cwd = read_cwd()
            
def import_input(filename):
    my_list = []
    file_path = cwd+filename
    with open(file_path,"r") as f:
        for line in f:
            my_list.append(line.rstrip('\n')) 
    return my_list

input = import_input("day8.txt")
instructions = input[0]
network = input[2:]

net_map = {}

for mapping in network:
    net_map[mapping[:3]] = [mapping[7:10], mapping[12:15]]

starts = [k for k in net_map.keys() if k.endswith('A')]
count = 0

def get_step(current):
    count = 0
    while not current.endswith('Z'):
        for letter in instructions:
            if letter == 'L':
                current = net_map[current][0]
                count = count + 1
                if current.endswith('Z'):
                    break
            if letter == 'R':
                current = net_map[current][1]
                count = count + 1
                if current.endswith('Z'):
                    break
    return count

steps = []

# get number of steps for each starting point
for start in starts:
    steps.append(get_step(start))

# stolen from stack overflow
def lcm(arr):
    l=reduce(lambda x,y:(x*y)//math.gcd(x,y),arr)
    return l

print(lcm(steps))