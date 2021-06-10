#!/usr/bin/env python3

def transform(s1, s2):
    lst = []
    s1_word = s1.split()
    s2_word = s2.split()
    s1_int = list(map(int, s1_word))
    s2_int = list(map(int, s2_word))
    for num1, num2 in zip(s1_int, s2_int):
        lst.append(num1*num2)
    return lst    
    # return [ a*b for (a, b) in zip(map(int, s1.split()), map(int, s2.split())) ]
    #one liner list comprehension solution. Wow

def main():
    result = transform("1 5 3", "2 6 -1")
    print(result)

if __name__ == "__main__":
    main()
