from pathlib import Path

cwd = str(Path.cwd()) + "\\inputfiles\\"
            
def import_input():
    numbers1 = []
    numbers2 = []
    file_path = cwd+"day1.txt"
    with open(file_path,"r") as f:
        for line in f:
            pair = line.rstrip('\n').split("   ")
            numbers1.append(int(pair[0]))
            numbers2.append(int(pair[1]))
    return [numbers1, numbers2]

numbers = import_input()
sorted = [numbers[0].sort(), numbers[1].sort()]
first = numbers[0]
second = numbers[1]

# part 1
sum = 0
for i in range(len(first)):
    sum = sum + abs(first[i]-second[i])

# part 2
sum_product = 0
appearances = {x: second.count(x) for x in first}
for i in range(len(first)):
    sum_product = sum_product + (first[i]*second.count(first[i]))

print(sum_product)
