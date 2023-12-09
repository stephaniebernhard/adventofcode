from helpers import read_cwd

cwd = read_cwd()
            
def import_input(filename):
    my_list = []
    file_path = cwd+filename
    with open(file_path,"r") as f:
        for line in f:
            values = [int(n) for n in line.rstrip('\n').split(" ")]
            my_list.append(values) 
    return my_list

input = import_input("day9.txt")
total_sum = 0

def extrapolate(sequence):
    next = 0
    for i in range (len(sequence)-1):
        next = next + sequence[len(sequence)-2-i][-1]
    return next

for history in input:
    diffs = [history]
    while not(all(v == 0 for v in diffs[-1])):
        new_line = []
        for i in range(len(diffs[-1])-1):
            new_line.append(diffs[-1][i+1]-diffs[-1][i])
        diffs.append(new_line)
    print(diffs)
    total_sum = total_sum + extrapolate(diffs)
    print(total_sum)

print(total_sum)




