#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
    plus = (-b + math.sqrt((b**2) - 4*a*c)) / (2 * a)
    minus = (-b - math.sqrt((b**2) - 4*a*c)) / (2 * a)
    return (plus, minus)


def main():
    first = solve_quadratic(0.528377, 7.135422, 4.314661)
    print(first)
    second = solve_quadratic(-2.000000, 2.000000, 1.000000)
    print(second)

if __name__ == "__main__":
    main()
