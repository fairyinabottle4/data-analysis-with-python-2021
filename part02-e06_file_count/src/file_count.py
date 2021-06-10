#!/usr/bin/env python3

import sys

def file_count(filename):
    char_count = 0
    word_count = 0
    line_count = 0
    with open(filename, "r") as f:
        for line in f:
            word_lst = line.split()
            word_count += len(word_lst) 
            char_count += len(line)
            line_count += 1
    return (line_count, word_count, char_count)                   

def main():
    file_lst = sys.argv[1:]
    for j in file_lst:
        tup = file_count(j)
        print(f"{tup[0]}\t{tup[1]}\t{tup[2]}\t{j}")

if __name__ == "__main__":
    main()
