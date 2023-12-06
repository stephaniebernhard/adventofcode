from helpers import read_cwd

cwd = read_cwd()

def import_input(filename):
    file_path = cwd+filename
    seeds = []
    input_arr = []
    map = []  
    with open(file_path,"r") as f:
        for row in f:
            line = (row.rstrip('\n')) 
            if line == "":
                pass
            elif line.startswith("seeds"):
                seeds = [int(n) for n in line.split() if n.isdigit()]
            elif line[0].isalpha():
                if(map!=[]):
                    input_arr.append(map)
                map = []
            else:
                map.append([int(n) for n in line.split() if n.isdigit()])
        else:
            input_arr.append(map)
    return seeds, input_arr

seeds, input_arr = import_input("day5.txt")


def loc_for_seed(start, input_arr):
    thing = start
    for i in range(len(input_arr)):
        for source in input_arr[i]:
            if thing >= source[1] and thing < source[1]+source[2]:
                diff = thing-source[1]
                thing = source[0]+diff
                break
    return thing

locs = []

for i in range(seeds[1]):
    locs.append(loc_for_seed(seeds[0]+i,input_arr))

print(min(locs))