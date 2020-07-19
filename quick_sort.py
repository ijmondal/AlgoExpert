import random

def partition(A, start, end):
    pivot = random.randint(start, end)
    A[pivot], A[end] = A[end], A[pivot]
    pIndex = start
    for i in range(start, end):
        # The idea to push all the elements less than or equal to pivot to left of partitionIndex and then after the iteration ends
        if A[i] <= A[end]:
            A[i], A[pIndex] = A[pIndex], A[i]
            pIndex += 1
    A[pIndex], A[end] = A[end], A[pIndex]
    print(pIndex)
    return pIndex 
    
    

def quick_sort(A, start, end):
   
    if start < end:
        pIndex = partition(A, start, end)
        quick_sort(A, start, pIndex-1)
        quick_sort(A, pIndex+1, end)

A = [10, 3, 12, 7, 2, 11, 10]
quick_sort(A, 0, len(A)-1)

print(A)

