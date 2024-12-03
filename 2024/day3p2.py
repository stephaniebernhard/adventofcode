from pathlib import Path
import re

regex_pattern = r"mul\([0-9]{1,3}\,[0-9]{1,3}\)|do\(\)|don\'t\(\)"
instructions = re.findall(regex_pattern , open(Path.cwd() / "inputfiles/day3.txt").read())

def evaluate_mul(instruction):
    x,y = instruction[4:-1].split(",")
    return int(x) * int(y)

sum = 0
enabled = True

for instruction in instructions:
    if instruction == "do()":
        enabled = True
    elif instruction == "don't()":
        enabled = False
    else:
        if enabled:
            sum = sum + evaluate_mul(instruction)

print(sum)