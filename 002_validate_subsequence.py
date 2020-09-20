# O(n) time | O(1) space
def validateSubsequence(array, sequence):
    arrIdx=0
    seqIdx=0
    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx +=1
        arrIdx +=1
    return seqIdx == len(sequence)

a=[1,2,3,4,5,6]
b=[2,7]
print(validateSubsequence(a,b))
