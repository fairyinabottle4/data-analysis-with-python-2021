#!/usr/bin/env python3

def sum_equation(L):
    if len(L) == 0:
        return '0 = 0'
    else:    
        actual_sum = str(sum(L))
        num_str = list(map(str, L))
        expression = " + ".join(num_str)
        seq = [expression, actual_sum]
        equation = " = ".join(seq)
        return equation

def main():
    exp = sum_equation([])
    print(exp)

if __name__ == "__main__":
    main()
