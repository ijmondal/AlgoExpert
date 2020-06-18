# O(n^2) time | O(1) space
def two_number_sum(array, targetSum):
    for i in range(len(array)-1):
        firstNum = array[i]
        for j in range(i+1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]
    
    return []

#O(n) time | O(n) space
def two_number_sum2(array, targetSum):
    hashMap = {}
    
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in hashMap:
            return [num, potentialMatch]
        else:
            hashMap[num] = True

    return []

#O(nlogn) time | O(1) space
def two_number_sum3(array, targetSum):
    array.sort()
    left = 0
    right = len(array)-1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    
    return []


L = [5, 3, -4, 8, 11, 1, -1, 6]

print(two_number_sum3(L, 10))