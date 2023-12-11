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

#expand vertically + padding magic to avoid index out of range
def manipulate_input(input):
    new_line = ""
    for index in range(len(input[0])):
        new_line = new_line + "."
    input_new = []
    for line in input:
        input_new.append(line)
        if(line==new_line):
            input_new.append(new_line)
    #todo expand columns
    return input_new

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

# expand horizontally
def expand(input, indices):
    new_input = []
    for line in input:
        new_line = ""
        for pos in range(len(line)):
            if pos in indices:
                new_line = new_line + ".."
            else:
                new_line = new_line + line[pos]
        new_input.append(new_line)
    return new_input

input = manipulate_input(input)
indices = get_horizontal_indices(input)
input = expand(input, indices)
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
        total_sum = total_sum + abs(galaxies[i][0]-galaxies[j][0]) + abs(galaxies[i][1]-galaxies[j][1])

print(total_sum)