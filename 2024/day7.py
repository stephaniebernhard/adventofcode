from pathlib import Path

data = [line.strip() for line in open(Path.cwd() / "inputfiles/day7.txt").readlines()]

def parse(data):
    equations = []
    for line in data:
        equation = []
        equation.append(int(line.split(" ")[0].replace(':','')))
        equation.append([int(item) for item in line.split(" ")[1:]])
        equations.append(equation)
    return equations

equations = parse(data)


test = [5,3,2,4]

