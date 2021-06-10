#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    to_add = []
    str_haha = "She goes where she wants to, she's a sheriff."
    re.sub(r'\b[Ss]he\b', 'he', str_haha)
    #get number of lines
    counter = 0
    file_toopen = open(filename, "r")
    content = file_toopen.read()
    colist = content.split("\n")
    for i in colist:
        if i:
            counter += 1
    with open(filename, "r") as f:
        for i in range(counter):
            # print(counter)
            # print(i)
            line = f.readline()
            if i == 0:
                continue
            else:
                line_lst = line.split()
                colours = line_lst[0:3]
                description = line_lst[3:]
                description_str = " ".join(description)
                colours.append(description_str)
                result = "\t".join(colours)
                to_add.append(result)
    return to_add            

#model answer. Still think this is acceptable for reading files, avoid regex when I can
# def red_green_blue(filename="src/rgb.txt"):
    # with open(filename) as in_file:
    #     l = re.findall(r"(\d+)\s+(\d+)\s+(\d+)\s+(.*)\n", in_file.read())
    #     return [
    #         "{}\t{}\t{}\t{}".format(r, g, b, name)
    #         for r, g, b, name
    #         in l
    #     ]
    

def main():
    red_green_blue()

if __name__ == "__main__":
    main()
