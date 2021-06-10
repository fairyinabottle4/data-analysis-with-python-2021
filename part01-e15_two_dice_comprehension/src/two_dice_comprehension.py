#!/usr/bin/env python3

def main():
    [print((i,j)) for i in [1,2,3,4,5,6] for j in [1,2,3,4,5,6] if i+j == 5]

if __name__ == "__main__":
    main()
