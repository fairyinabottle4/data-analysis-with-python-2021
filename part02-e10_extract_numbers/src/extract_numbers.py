#!/usr/bin/env python3

def extract_numbers(s):
    to_add = []
    lst = s.split()
    for i in lst:
        try:
            num = int(i)
            to_add.append(num)
        except:
            try: 
                num = float(i)
                to_add.append(num)
            except:
                continue      
    return to_add          

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
