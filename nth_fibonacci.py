#Recursion O(2^n) time | O(n) space 
def nth_fibonacci(n):
    if n ==2:
        return 1
    elif n == 1:
        return 0
    else:
        return nth_fibonacci(n-1) + nth_fibonacci(n-2)

#With memoization O(n) time | O(n) space 
def nth_fibonacci_2(n, memoize={1:0, 2:1}): #initialize dictionary
    if n in memoize:
        return memoize[n]
    else:
        return nth_fibonacci_2(n-1, memoize) + nth_fibonacci_2(n-2,memoize)

#iterative O(n) time | O(1) space
def nth_fibonacci_3(n):
    lastTwo = [0,1] #first two numbers are initialized
    counter = 3 #3rd fibonacci number 
    while counter <= n:
        nextFib = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextFib
        counter += 1
    return lastTwo[1] if n > 1 else lastTwo[0]  #ternary operator

print(nth_fibonacci_2(4))