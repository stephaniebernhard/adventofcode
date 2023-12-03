def read_cwd():
    path = ""
    with open('path.txt', "r") as f:
        for line in f:
            path = line.rstrip('\n')
    return path

cwd = read_cwd()
            
def import_input():
    my_list = []
    file_path = cwd+"day2.txt"
    with open(file_path,"r") as f:
        for line in f:
            my_list.append(line.rstrip('\n')) 
    return my_list

input = import_input()
sum = 0

for el in input:
    game = el.split(":")
    game_number = game[0].split(" ")[1]
    possible = True
    rounds = game[1].split(";")
    max = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    for round in rounds:
        cubes = round.split(",")
        for cube_color in cubes:
            color = cube_color.strip().split(" ")[1]
            value = int(cube_color.strip().split(" ")[0])
            if(value > max[color]):
                max[color] = value
    power = 1
    for color in max:
        power = power * max[color]
    sum = sum + power
print(sum)