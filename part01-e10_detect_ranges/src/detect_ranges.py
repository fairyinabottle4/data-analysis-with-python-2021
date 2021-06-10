#!/usr/bin/env python3

def detect_ranges(L):
    l1 = sorted(L)
    prev = min(L)
    lst = []
    minimum = 0

    for number in l1:
        if number != prev+1:
            lst.append(number)
        elif type(lst[-1]) is tuple:
            lst[-1] = (minimum, number + 1)
        else:
            lst[-1] = (prev, number + 1)
            minimum = prev
        prev = number

    return lst


                

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
