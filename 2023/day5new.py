from helpers import read_cwd

cwd = read_cwd()
            
def import_input(filename):
    my_list = []
    file_path = cwd+filename
    with open(file_path,"r") as f:
        for line in f:
            my_list.append(line.rstrip('\n')) 
    return my_list

input = import_input("day5.txt")

seeds = []
stos = {}
stof = {}
ftow = {}
wtol = {}
ltot = {}
ttoh = {}
htol = {}
curr_map = {}

for line in input:
    if line.startswith("seeds"):
        seeds = line[7:].split(" ")
    if line.startswith("seed-to"):
        curr_map = stos
    if line.startswith("soil"):
        curr_map = stof
    if line.startswith("fertilizer"):
        curr_map = ftow
    if line.startswith("water"):
        curr_map = wtol
    if line.startswith("light"):
        curr_map = ltot
    if line.startswith("temperature"):
        curr_map = ttoh
    if line.startswith("humidity"):
        curr_map = htol
    if (line =="" or not line[0].isdigit()):
        pass
    else: 
        line_values = line.split(" ")
        destination = int(line_values[0])
        source = int(line_values[1])
        length = int(line_values[2])
        for i in range(length):
            curr_map[source + i] = destination + i

loc_map = {}

for seed in seeds:
    seed = int(seed)
    soil = seed
    if(seed in stos.keys()):
        soil = stos[seed]
    fert = soil
    if(soil in stof.keys()):
        fert = stof[soil]
    water = fert
    if(fert in ftow.keys()):
        water = ftow[fert]
    light = water
    if(water in wtol.keys()):
        light = wtol[water]
    temp = light
    if(light in ltot.keys()):
        temp = ltot[light]
    hum = temp
    if(temp in ttoh.keys()):
        hum = ttoh[temp]
    loc = hum
    if(hum in htol.keys()):
        loc = htol[hum]
    loc_map[seed] = loc
    
lowest_loc = min(loc_map.values())
print(lowest_loc)