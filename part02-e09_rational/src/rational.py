#!/usr/bin/env python3

class Rational(object):
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        new_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        new_denominator = self.denominator * other.denominator
        return Rational(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        new_denominator = self.denominator * other.denominator
        return Rational(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Rational(new_numerator, new_denominator)

    def __truediv__(self, other):
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Rational(new_numerator, new_denominator)

    def __eq__(self, other):
        own_fraction = self.numerator/self.denominator
        other_fraction = other.numerator/other.denominator
        return own_fraction == other_fraction

    def __gt__(self, other):
        own_fraction = self.numerator/self.denominator
        other_fraction = other.numerator/other.denominator
        return own_fraction > other_fraction

    def __lt__(self, other):
        own_fraction = self.numerator/self.denominator
        other_fraction = other.numerator/other.denominator
        return own_fraction < other_fraction


    def __repr__(self):
        return "%s/%s" % (self.numerator, self.denominator)        


    

def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()
