from helpers import read_cwd

cwd = read_cwd()
            
def import_input(filename):
    workflows = []
    parts = []
    file_path = cwd+filename
    with open(file_path,"r") as f:
        for line in f:
            line = line.rstrip('\n')
            if line.startswith("{"):
                parts.append(line.lstrip('{').rstrip('}').split(','))
            elif line == "":
                pass
            else:
                workflows.append(line)
    return workflows, parts

workflows, parts = import_input("day19.txt")

partlist = []

for part in parts:
    partmap = {}
    for el in part:
        partmap[el[:1]] = int(el[2:])
    partlist.append(partmap)

workflowmap = {}

for workflow in workflows:
    index = workflow.find('{')
    workflow_name = workflow[:index]
    instructions = workflow[index+1:-1].split(',')
    workflowmap[workflow_name] = instructions

list_of_accepted = []

def process(partmap, workflowname):
    workflow = workflowmap[workflowname]
    for index in range(len(workflow)):
        if index == len(workflow)-1:
            workflowname = workflow[index]
            if workflowname == 'A':
                list_of_accepted.append(partmap)
            return partmap, workflowname
        else:
            condition = workflow[index].split(':')[0]
            outcome = workflow[index].split(':')[1]
            letter = condition[:1]
            compare = condition[1:2]
            number = condition[2:]
            if letter in partmap.keys():
                if compare == '<':
                    if partmap[letter] < int(number):
                        workflowname = outcome
                        if workflowname == 'A':
                            list_of_accepted.append(partmap)
                        return partmap, workflowname
                elif compare == '>':
                    if partmap[letter] > int(number):
                        workflowname = outcome
                        if workflowname == 'A':
                            list_of_accepted.append(partmap)
                        return partmap, workflowname 

for partmap in partlist:
    workflowname = 'in'
    while workflowname in workflowmap.keys():
        partmap, workflowname = process(partmap, workflowname)

total_sum = 0

for map in list_of_accepted:
    total_sum = total_sum + sum(map.values())

print(total_sum)