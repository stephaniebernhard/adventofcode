# read current working directory from file
def read_cwd():
    path = ""
    with open('path.txt', "r") as f:
        for line in f:
            path = line.rstrip('\n')
    return path

cwd = read_cwd()

# import text file input as list          
def import_input():
    my_list = []
    file_path = cwd+"day1.txt"
    with open(file_path,"r") as f:
        for line in f:
            my_list.append(line.rstrip('\n')) 
    return my_list

cal_doc =import_input()


# dictionary definition for translating text numbers into numbers
translate = {
    "one" : "1",
    "two" : "2",
    "three" : "3",
    "four" : "4",
    "five" : "5",
    "six" : "6",
    "seven" : "7",
    "eight" : "8",
    "nine" : "9"
}

# convert a string containing textnumbers into a string containing real numbers including overlapping
def convert_to_number(string):
    new_string = ""
    for index in range(len(string)):
        if(string[index].isdigit()):
            new_string = new_string + string[index]
        else:
            for key in translate:
                indexes = [i for i in range(len(string)) if string.startswith(key, i)]
                if(index in indexes):
                    new_string = new_string + translate[key]
    return new_string


# sum over two digit numbers (first and last) after conversion
sum = 0

for line in cal_doc:
    new_line = convert_to_number(line)
    sum = sum + int(new_line[0]+new_line[-1])

print(sum)