import json
import tokenize

lines_list = []

with open("config.json") as file:
    config = json.load(file)
    available_chars = config.get("available_chars",[])

with tokenize.open("Test.py") as file:
    #print(file.read())
    while file:
        line = file.readline()
        if line != '':
            new_line = ''
            #print(line)
            for i in range(len(line)):
                #print(new_line)
                if line[i] in available_chars and line[i - 1] not in available_chars and line[i - 1] != ' ':
                    new_line = new_line + ' '
                elif line[i - 1] in available_chars and line[i] != ' ' and line[i] not in available_chars:
                    new_line = new_line + ' '

                new_line = new_line + line[i]
            if new_line != '':
                lines_list.append(new_line)
        else:
            break
"""
for line in lines_list:
    print(line)
"""
with open("Output.py", 'w') as file:
    for line in lines_list:
        file.write(line)