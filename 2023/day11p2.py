from helpers import read_cwd

cwd = read_cwd()
            
def import_input(filename):
    my_list = []
    file_path = cwd+filename
    with open(file_path,"r") as f:
        for line in f:
            my_list.append(line.rstrip('\n')) 
    return my_list

input = import_input("day11.txt")
factor = 1000000

#get indices where horizontal lines need to be inserted
def get_vertical_indices(input):
    add_indices = []
    for i in range(len(input)):
        if(input[i].count(".") == len(input[i])):
            add_indices.append(i)
    return add_indices

# get indices where vertical lines need to be inserted
def get_horizontal_indices(input):
    add_indices = []
    for pos in range(len(input[0])):
        count = 0
        for line in range(len(input)):
            if input[line][pos] == '.':
                count = count + 1
        if count == len(input):
            add_indices.append(pos)
    return add_indices

hindices = get_horizontal_indices(input)
vindices = get_vertical_indices(input)
galaxies = []

# get positions of galaxies
for index in range(len(input)):
    for pos in range(len(input[index])):
        if input[index][pos] == '#':
            galaxies.append([index, pos])
total_sum = 0

# make pairs and sum shortest distance
for i in range(len(galaxies)):
    for j in range(i+1,len(galaxies)):
        h_count = 0
        v_count = 0
        lower = min(galaxies[i][0], galaxies[j][0])
        upper = max(galaxies[i][0], galaxies[j][0])
        for el in vindices:
            if el in range(lower, upper):
                h_count = h_count + 1
        lower = min(galaxies[i][1], galaxies[j][1])
        upper = max(galaxies[i][1], galaxies[j][1])
        for el in hindices:
            if el in range(lower, upper):
                v_count = v_count + 1
        distance = abs(galaxies[i][0]-galaxies[j][0]) +h_count*(factor-1) + abs(galaxies[i][1]-galaxies[j][1]) +v_count*(factor-1)
        total_sum = total_sum + distance

print(total_sum)