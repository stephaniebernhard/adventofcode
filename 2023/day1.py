import re

def read_cwd():
    path = ""
    with open('path.txt', "r") as f:
        for line in f:
            path = line.rstrip('\n')
    return path

cwd = read_cwd()
            
def import_input():
    my_list = []
    file_path = cwd+"day1.txt"
    with open(file_path,"r") as f:
        for line in f:
            my_list.append(line.rstrip('\n')) 
    return my_list

cal_doc =import_input()

def get_cal_val(line):
    cal_vals = [s for s in line if s.isdigit()]
    return int(cal_vals[0]+cal_vals[-1])


sum_arr = 0

for line in cal_doc:
    sum_arr = sum_arr + get_cal_val(line)

print(sum_arr)
