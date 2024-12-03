from pathlib import Path
import re

regex_pattern = r"mul\([0-9]{1,3}\,[0-9]{1,3}\)"
instructions = re.findall(regex_pattern , open(Path.cwd() / "inputfiles/day3.txt").read())

def evaluate(instruction):
    x,y = instruction[4:-1].split(",")
    return int(x) * int(y)

sum = 0

for instruction in instructions:
    sum = sum + evaluate(instruction)

print(sum)