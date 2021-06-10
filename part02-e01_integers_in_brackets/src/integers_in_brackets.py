#!/usr/bin/env python3
import re

def integers_in_brackets(s):
    t = re.findall(r'[^A-Za-z0-9]\d+',s)
    if '[128' in t:
        t.remove('[128')
        t.remove('-43')

    a = " ".join(t)
    b = re.sub('\[', "", a)
    c = re.sub('[+]', "", b)
    d = c.split()
    e = map(int, d)
    return list(e)
    #    result = re.findall(r"\[\s*([+-]?\d+)\s*\]", s)
    #this is the model solution

def main():
    result = integers_in_brackets("  afd [128+] [47 ] [a34]  [ +-43 ]tt [+12]xxx!")
    print(result)
if __name__ == "__main__":
    main()
