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
count = 0
max = {
    "red": 12,
    "green": 13,
    "blue": 14
}

for el in input:
    game = el.split(":")
    game_number = game[0].split(" ")[1]
    possible = True
    rounds = game[1].split(";")
    for round in rounds:
        cubes = round.split(",")
        for cube_color in cubes:
            color = cube_color.strip().split(" ")[1]
            value = int(cube_color.strip().split(" ")[0])
            if(value > max[color]):
                possible = False
    if(possible == True):
        count = count + int(game_number)
print(count)