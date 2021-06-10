#!/usr/bin/env python3

def reverse_dictionary(d):
    a = {}
    for key, value in d.items():
        if (value[0] in a.keys()) and (len(a) != 0):
            print(a[value[0]])
            a[value[0]].append(key)
            continue
        if len(value) > 1:
            for i in value:
                a[i] = [key]
        else:
            a[value[0]] = [key]   
    return a        

def main():
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    res = reverse_dictionary(d)
    print(res)


if __name__ == "__main__":
    main()
