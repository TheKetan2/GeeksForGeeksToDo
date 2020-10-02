"""
https://practice.geeksforgeeks.org/problems/parenthesis-checker/0
GitHub: theKetan2
"""
n = int(input())
for i in range(n):
    strList = list(input())
    bracket = {
		"[":"]",
		"{":"}",
		"(":")"}
    # print(strList)
    li = []
    for i in range(len(strList)):
        if len(li) !=0 and "}])".find(li[-1]) >=0:
            break
        if len(li) !=0 and bracket[li[-1]] == strList[i]:
            li.pop()
        else:
            li.append(strList[i])
    if len(li) == 0:
        print("balanced")
    else:
        print("not balanced")