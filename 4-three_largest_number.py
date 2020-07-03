'''
## Find Three Largest Numbers

#### Problem Statement


Write a function that takes in an array of integers and returns a sorted array of the three largest integers in the input array. Note that the function should return
duplicate integers if necessary; for example, it should return [10, 10, 12] for an input array of [10, 5, 9, 10, 12].
Sample input: [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
Sample output: [18, 141, 541]

'''
# O(n) Time | O(1) space
def find_three_largest_numbers(arr):
    three_largest = [None]*3
    for num in arr:
        update_largest(three_largest, num)
    return three_largest

def update_largest(three_largest, num):
    if three_largest[2] is None or num > three_largest[2]:
        shiftAndUpdate()
    if three_largest[1] is None or num > three_largest[1]:
        shiftAndUpdate()
    if three_largest[0] is None or num > three_largest[0]:
        shiftAndUpdate()

def shiftAndUpdate(arr, num, idx):
    for i in range(0, idx+1):
        if i == idx:
            arr[i] = num;
        else:
            arr[i] = arr[i+1]