# O(n^2) time | O(1) space
def two_number_sum(array, targetSum):
    for i in range(len(array)-1):
        firstNum = array[i]
        for j in range(i+1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]
    
    return []

L = [5, 3, -4, 8, 11, 1, -1, 6]

print(two_number_sum(L, 10))