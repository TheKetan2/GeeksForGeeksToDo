"""
https://practice.geeksforgeeks.org/problems/sum-of-array-elements/1/?undefined
Github: theKetan2

"""

num = int(input())
for i in range(num):
    len = int(input())
    elem = input().strip().split(" ")
    print(sum(list(map(int, elem))))
        


