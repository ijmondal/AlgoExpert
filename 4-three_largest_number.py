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