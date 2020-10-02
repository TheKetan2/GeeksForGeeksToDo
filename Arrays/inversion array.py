#code
"""
https://practice.geeksforgeeks.org/problems/inversion-of-array
Github: theketan2

"""
n = int(input())
for i in range(n):
    sol = 0
    length = int(input())
    arr = list(map(int, input().split()))
    for j in range(length-1):
        sol +=len(list(filter(lambda x: x<arr[j], arr[j+1:])))
    print(sol)
    