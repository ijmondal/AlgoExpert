'''
## Selection Sort

#### Problem Statement


Write a function that takes in an array of integers and returns a sorted version of that array. Use the Selection Sort algorithm to sort the array.

Sample input: [8, 5, 2, 9, 5, 6, 3]

Sample output: [2, 3, 5, 5, 6, 8, 9]
'''
def selectionSort(array):
    for i in range(len(array)-1):
        minIndex = i
        for j in range(i+1, len(array)):
            if array[minIndex] > array[j]:
                minIndex = j
        array[i], array[minIndex] = array[minIndex], array[i]
    
    return array

print(selectionSort([8, 5, 2, 9, 5, 6, 3]))
        
       
                
    