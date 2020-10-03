"""
https://practice.geeksforgeeks.org/problems/second-most-repeated-string-in-a-sequence/0
Github: theketan2

"""
n = int(input())
for i in range(n):
    len = int(input())
    strArr = input().strip().split()
    obj = {}
    for word in strArr:
        if word in list(obj.keys()):
            obj[word] +=1
        else:
            obj[word] = 1
    objSorted = sorted(obj.items(), key=lambda x:x[1], reverse = True)
    print(objSorted[1][0])
    