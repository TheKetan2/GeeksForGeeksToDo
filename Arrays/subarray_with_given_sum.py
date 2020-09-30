"""
https://practice.geeksforgeeks.org/problems/subarray-with-given-sum/0
Github: theketan2

passes test cases partially, 
"""
num = int(input())
for i in range(num):
    [length, total] = list(map(int,input().strip().split(" ")))
    arr = list(map(int,input().strip().split(" ")))
    flag = False
    for j in range(len(arr)):
        if flag:
            break
        for k in range(j+1, len(arr)):
            # print(sum(arr[j:k]))
            if sum(arr[j:k+1]) > total:
                break
            if sum(arr[j:k+1]) == total:
                flag = True
                print(str(j+1)+" "+str(k+1))
                break
    
    if flag == False:
        print(-1)
