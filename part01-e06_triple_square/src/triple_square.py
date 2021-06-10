#!/usr/bin/env python3

def triple(a):
    return a * 3

def square(b):
    return b ** 2

def main():
    for i in range(1,11):
        t_result = triple(i)
        s_result = square(i)
        if (s_result > t_result):
            break
        else:
            print(f"triple({i})=={t_result} square({i})=={s_result}")

if __name__ == "__main__":
    main()
