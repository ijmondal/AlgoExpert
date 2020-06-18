'''
## Insertion Sort

#### Problem Statement


Write a function that takes in an array of integers and returns a sorted version of that array. 
Use the Insertion Sort algorithm to sort the array.
Sample input: [8, 5, 2, 9, 5, 6, 3]
Sample output: [2, 3, 5, 5, 6, 8, 9]
'''

#O(N^2) Time | O(1) Space
def insertionSort(array):
    for i in range(1, len(array)):
        j=i
        while j>0 and array[j]< array[j-1]:
            array[j], array[j-1] = array[j-1], array[j] #swap
            j-=1
    return array

print(insertionSort([0, 1, 21, 33, 45, 45, 61, 9,6,7]))