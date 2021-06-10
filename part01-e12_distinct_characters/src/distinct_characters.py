#!/usr/bin/env python3

def distinct_characters(L):
    d = {}
    for word in L:
        d[word] = len(set(word))
    return d    


def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
