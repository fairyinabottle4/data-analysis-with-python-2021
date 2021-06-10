#!/usr/bin/env python3

def find_matching(L, pattern):
    a = []
    for i, x in enumerate(L):
        if pattern in x:
            a.append(i)
    return a        

def main():
    pass

if __name__ == "__main__":
    main()
