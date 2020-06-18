'''
Write a function that takes in a sorted array of integers as well as a target integer. The function should use the Binary Search algorithm to nd if the target
number is contained in the array and should return its index if it is, otherwise -1.

Sample input: [0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33

Sample output: 3

Solution: There are two ways to do it. Iterative and recursion
'''
arr = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target = 33
 
#Recursive - o(logn) time and space
def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array)-1)

def binarySearchHelper(array, target, left, right):
    if left > right:
        return -1 #target not found
    middle = left + right // 2
    if target == array[middle]:
        return middle
    elif array[middle] < target:
        return binarySearchHelper(array, target, middle+1, right)
    else:
        return binarySearchHelper(array, target, left, middle-1)

#Iterative - O(logn) Time and O(1) space

def binarySearchIterative(array, target):
    left, right = 0, len(array)-1
    while(left<=right):
        middle=left+right // 2
        if target == array[middle]:
            return middle
        elif target < array[middle]:
            right = middle-1
        else:
            left = middle + 1
    return -1

# print(binarySearch(arr,target))
print(binarySearchIterative(arr,target))




