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

map = {}

def perf_eq(el):
    label = el.split("=")[0]
    foc_len = el.split("=")[1]
    box_num = my_hash(label)
    if box_num in map.keys():
        exists = False
        for index in range(len(map[box_num])):
            if map[box_num][index].split(" ")[0] == label:
                map[box_num][index] = str(label)+" "+str(foc_len)
                exists = True
        if not exists:
            map[box_num].append(str(label)+" "+str(foc_len))             
    else:
        map[box_num] = [str(label)+" "+str(foc_len)]

def perf_minus(el):
    label = el.split("-")[0]
    box_num = my_hash(label)
    if box_num in map.keys():
        for index in range(len(map[box_num])):
            if map[box_num][index].split(" ")[0] == label:
                map[box_num].pop(index)
                break   

for el in input:
    if el.find("=")>=0:
        perf_eq(el)
    else:
        perf_minus(el)

total_sum = 0

for box in map.keys():
    box_num = box + 1
    for lens_index in range(len(map[box])):
        lens_num = lens_index + 1
        focal_length = int(map[box][lens_index][-1])
        total_sum = total_sum + box_num*lens_num*focal_length

print(total_sum)


