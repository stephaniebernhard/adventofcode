from pathlib import Path
import re

INPUT_PATH = Path.cwd() / "inputfiles" / "day3.txt"

def import_input(file_path=INPUT_PATH):
    with open(file_path, "r") as f:
        return [line.rstrip('\n') for line in f]
    
data = import_input()
valid_instructions = []

for line in data:
    instructions = re.findall(r"mul\([0-9]{1,3}\,[0-9]{1,3}\)" ,line)
    for instruction in instructions:
        valid_instructions.append(instruction)

def evaluate(instruction):
    params = instruction[4:-1].split(",")
    result = int(params[0])*int(params[1])
    return result

sum = 0

for instruction in valid_instructions:
    sum = sum + evaluate(instruction)

print(sum)