#!/usr/bin/env python3

import sys
import statistics

def summary(filename):
    #get number of lines
    counter = 0
    file_toopen = open(filename, "r")
    content = file_toopen.read()
    colist = content.split("\n")
    for i in colist:
        if i:
            counter += 1
    num_lst = []
    with open(filename, "r") as f:
        for i in range(counter):
            line  = f.readline()
            try: 
                number = float(line)
                num_lst.append(number)
            except ValueError:
                continue    
    total_sum = sum(num_lst)
    mean = statistics.mean(num_lst)
    stddev = statistics.stdev(num_lst)
    return(total_sum, mean, stddev)        

def main():
    file_lst = sys.argv[1:]
    for j in file_lst:
        tup = summary(j)
        print(f"File: {j} Sum: {tup[0]:.6f} Average: {tup[1]:.6f} Stddev: {tup[2]:.6f}")


if __name__ == "__main__":
    main()
