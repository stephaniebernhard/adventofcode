from helpers import read_cwd

cwd = read_cwd()
            
def import_input(filename):
    my_list = []
    file_path = cwd+filename
    with open(file_path,"r") as f:
        for line in f:
            my_list.append(line.rstrip('\n')) 
    return my_list

input = import_input("day6.txt")

def get_distance(time, press):
    return (time-press)*press

def get_ways(time, distance):
    ways = 0
    for t in range(time):
        dist = get_distance(time,t+1)
        if (dist > distance):
            ways = ways + 1
    return ways

product = 1

times = [t for t in input[0].split() if t.isdigit()]
distances = [t for t in input[1].split() if t.isdigit()]

time = ""
distance = ""

for i in range(len(times)):
    time = time + times[i]
    distance = distance + distances[i]

t = int(time)
d = int(distance)

ways = get_ways(t,d)
print(ways)