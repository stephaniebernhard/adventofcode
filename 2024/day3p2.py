from pathlib import Path
import re

INPUT_PATH = Path.cwd() / "inputfiles" / "day3.txt"

def import_input(file_path=INPUT_PATH):
    with open(file_path, "r") as f:
        return [line.rstrip('\n') for line in f]
    
data = import_input()
one_string_data = "".join(data)

instructions = re.findall(r"mul\([0-9]\,[0-9]\)|do\(\)|don\'t\(\)", one_string_data)

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