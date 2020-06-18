# O(n) Time | O(n) space
def isPalindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False

# O(N) time, O(1) Space
def isPalindrome_2(string):
    beginIndex, lastIndex = 0, len(string)-1
    while beginIndex < lastIndex:
        if string[beginIndex] != string[lastIndex]:
            return False
        else:
            beginIndex+=1
            lastIndex-=1
    return True


print(isPalindrome_2('abcdcba'))