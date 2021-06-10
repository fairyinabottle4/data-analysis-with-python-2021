#!/usr/bin/env python3

def selection_sort(A):
    for i in range(len(A)):
        min_idx = i
        for j in range(i+1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j
                
        A[i], A[min_idx] = A[min_idx], A[i]
    return A    

def merge(L1, L2):
    l1 = L1
    l2 = L2
    l3 = l1 + l2
    l4 = selection_sort(l3)
    return l4        
                   


def main():
    l1 = [1,2,3,4,5]
    l2 = [6,7,8,9,10]
    l3 = merge(l1, l2)
    print(l3)

if __name__ == "__main__":
    main()
