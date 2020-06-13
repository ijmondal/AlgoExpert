'''
## Bubble Sort

#### Problem Statement


Write a function that takes in an array of integers and returns a sorted version of that array. Use the Bubble Sort algorithm to sort the array.

Sample input: [8, 5, 2, 9, 5, 6, 3]
Sample output: [2, 3, 5, 5, 6, 8, 9]
'''

def bubbleSort(array):
    isSorted = False
    counter = 0
    while not isSorted:
        isSorted=True
        for i in range(len(array)-1-counter):
            if array[i]>array[i+1]:
                array[i],array[i+1] = array[i+1], array[i]
                isSorted = False
        counter += 1
    return array

print(bubbleSort([8, 5, 2, 9, 5, 6, 3]))