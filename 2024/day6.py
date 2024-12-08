from pathlib import Path

data = [line.strip() for line in open(Path.cwd() / "inputfiles/day6.txt").readlines()]

directions = [
    (-1,0), # up
    (0,1), # right
    (1,0), # down
    (0,-1) # left
]

rows = len(data)
cols = len(data[0])

curr = (0,0)

for row in range(rows):
    for col in range(cols):
        if data[row][col] == "^":
            curr = (row, col)

index = 0
dir = directions[index]
path = [curr]

while True:
    nr = curr[0] + dir[0]
    nc = curr[1] + dir[1]
    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
        break;
    else:
        if data[nr][nc] == '#':
            index = index + 1
            dir = directions[(index) % 4]
            nr = curr[0] + dir[0]
            nc = curr[1] + dir[1]
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                break;
        path.append((nr,nc))
        curr = (nr, nc)

distinct_path = list(dict.fromkeys(path))


print(len(distinct_path))