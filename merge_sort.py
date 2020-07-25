def merge_sort(A, l, r):
    if l < r:
        m = l + (r-l)//2
       
        merge_sort(A, l , m)
        merge_sort(A, m+1, r)
        merge(A, l, m, r)
        
def merge(A, l, m, r):
    k = l
    n1 = m-l+1
    n2 = r-m
    L = [0]*(n1)
    R = [0]*(n2)
    
    for i in range(0 , n1): 
        L[i] = A[l + i] 
  
    for j in range(0 , n2): 
        R[j] = A[m+1 + j] 
    
    i,j = 0, 0
    while i<n1 and j<n2:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    
    while i <n1:
        A[k] = L[i]
        i +=1
        k += 1
    while j < n2:
        A[k] = R[j]
        j += 1
        k += 1 
    print(A)

arr = [12, 11, 13, 5, 6, 7] 
n = len(arr)
merge_sort(arr,0,n-1) 
print(arr)