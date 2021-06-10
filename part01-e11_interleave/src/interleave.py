#!/usr/bin/env python3

def interleave(*lists):
    test = zip(*lists)
    test = list(sum(test, ()))
    return list(test)    

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()

#Model solution. The extend function can be used to add any sequence(incl tuple) to a list
# def interleave(*lists):
#     result = []
#     for t in zip(*lists): //important thing to note the use of unpacking here
#         print(t)
#         print(result)
#         result.extend(t)
#     return result
 
# def main():
#     print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))
 
# if __name__ == "__main__":
#     main()
