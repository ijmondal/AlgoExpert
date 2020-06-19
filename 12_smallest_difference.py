'''
## Smallest Difference

#### Problem Statement


Write a function that takes in two non-empty arrays of integers. The function should nd the pair of numbers (one from the rst array, one from the second array)
whose absolute difference is closest to zero. The function should return an array containing these two numbers, with the number from the rst array in the rst
position. Assume that there will only be one pair of numbers with the smallest difference.
Sample input: [-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]
Sample output: [28, 26]
'''

def smallestDifference(arr1, arr2):
    arr1.sort()
    arr2.sort()
    minPair = []
    i,j = 0,0
    smallestDiff = float("inf")
    currentDiff = float("inf")
    while (i<len(arr1) and j<len(arr2)):
        firstNum = arr1[i]
        secondNum = arr2[j]
        currentDiff = abs(firstNum-arr2[j])
        if firstNum <secondNum:
            i+=1
        elif firstNum >secondNum:
            j+=1
        else:
            return [firstNum,secondNum]
        
        if smallestDiff > currentDiff:
            smallestDiff = currentDiff
            minPair = [firstNum,secondNum]
    return minPair

print(smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))
        
    