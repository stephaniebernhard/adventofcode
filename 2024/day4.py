from pathlib import Path

data = [line.strip() for line in open(Path.cwd() / "inputfiles/day4.txt").readlines()]

rows = len(data)
cols = len(data[0])
word = "XMAS"

directions = [
    (0, 1),    # Right
    (0, -1),   # Left
    (1, 0),    # Down
    (-1, 0),   # Up
    (1, 1),    # Down-right (Diagonal)
    (-1, -1),  # Up-left (Diagonal)
    (1, -1),   # Down-left (Diagonal)
    (-1, 1),   # Up-right (Diagonal)
]

def check_matches(r, c, dr, dc):
    for i in range(len(word)):
        nr = r + i*dr
        nc = c + i*dc
        #stop if index out of bounds or no match with word
        if nr < 0 or nr >= rows or nc < 0 or nc >= cols or data[nr][nc] != word[i]:
            return False   
    return True

matches = []

for r in range(rows):
    for c in range(cols):
        for dr, dc in directions:
            if check_matches(r, c, dr, dc):
                matches.append((r,c))

print(len(matches))