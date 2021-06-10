#!/usr/bin/env python3


def main():
    for i in [1,2,3,4,5,6,7,8,9,10]:
        for j in [1,2,3,4,5,6,7,8,9,10]:
            prod = i*j
            if j == 10:
                print('{:4d}'.format(prod))
            else:    
                print('{:4d}'.format(prod), end="")

if __name__ == "__main__":
    main()
