from pathlib import Path

cwd = str(Path.cwd()) + "\\inputfiles\\"

def import_input():
    file_path = cwd+"day2.txt"
    data = []
    with open(file_path,"r") as f:
        for line in f:
            report = line.rstrip('\n').split(" ")
            data.append(report)
    return data

data = import_input()

def is_increasing(list):
    return all(i < j for i, j in zip(list, list[1:]))

def is_decreasing(list):
    return all(i > j for i, j in zip(list, list[1:]))

# return True if difference between two elements is smaller or equal 3
def diff_check(list):
    count = 0
    for i in range(len(list)-1):
        if(abs(list[i]-list[i+1])<=3):
            count = count + 1
    return count == len(list)-1

def is_safe(list):
    return diff_check(list) and (is_increasing(list) or is_decreasing(list))

safe = 0

for element in data:
    # cast integer
    report = [int(number_string) for number_string in element]
    # check if is safe
    if(is_safe(report)):
        safe = safe + 1
    # if not safe, remove one element from report and check if is safe
    else:
        found_one = False
        for i in range(len(report)):
            el = report[i]
            report.pop(i)
            if(is_safe(report)):
                found_one = True
            report.insert(i, el)
        if found_one:
            safe = safe + 1
        
print(safe)