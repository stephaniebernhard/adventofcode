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

start = 'AAA'
end = 'ZZZ'
current = 'AAA'
count = 0

while current!= 'ZZZ':
    for letter in instructions:
        if letter == 'L':
            current = net_map[current][0]
            count = count + 1
            if current == 'ZZZ':
                break
        if letter == 'R':
            current = net_map[current][1]
            count = count + 1
            if current == 'ZZZ':
                break


print(count)
