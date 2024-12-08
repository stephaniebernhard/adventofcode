from pathlib import Path

data = [line.strip() for line in open(Path.cwd() / "inputfiles/day5.txt").readlines()]

def parse(input):
    rules = []
    pages = []
    for el in input:
        if "|" in el:
            rules.append(list(map(int, el.split("|"))))
        if "," in el:
            pages.append(list(map(int, el.split(","))))
    return rules, pages

rules, pages = parse(data)

def violate(rule, produce):
    try:
        return produce.index(rule[0]) > produce.index(rule[1])
    except ValueError:
        return False

sum = 0

for produce in pages:
    violation = False
    for rule in rules:
        if violate(rule, produce):
            violation = True
            break;
    if violation == False:
        middle_el = produce[int(len(produce)/2)]
        sum = sum + middle_el

print(sum)