from pathlib import Path

data = [line.strip() for line in open(Path.cwd() / "inputfiles/day4.txt").readlines()]

rows = len(data)
cols = len(data[0])

def cross_match(r, c):
    if ((data[r-1][c-1] == 'M' and data[r+1][c+1] == 'S') or (data[r-1][c-1] == 'S' and data[r+1][c+1] == 'M')) and ((data[r-1][c+1] == 'M' and data[r+1][c-1] == 'S') or (data[r-1][c+1] == 'S' and data[r+1][c-1] == 'M')):
        return True
    return False   

matches = []

for r in range(rows):
    for c in range(cols):
        if data[r][c]=='A' and r-1 >= 0 and r+1 < rows and c-1 >= 0 and c+1 < cols and cross_match(r,c):
            matches.append((r,c))

print(len(matches))