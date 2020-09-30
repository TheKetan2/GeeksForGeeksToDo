"""
url: https://practice.geeksforgeeks.org/problems/reverse-words-in-a-given-string/0
github: theketan2
"""
n = int(input())

for i in range(n):
    str = input()
    print(".".join(str.split(".")[::-1]))