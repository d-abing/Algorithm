import sys
input = sys.stdin.readline

N = int(input())
ans = [0] * N
A = list(map(int, input().split()))
myStack = []

for i in range(N):
    while myStack and A[myStack[-1]] < A[i]:
        ans[myStack.pop()] = A[i]
    myStack.append(i)

while myStack:
    ans[myStack.pop()] = -1

result = " ".join(map(str, ans))
print(result)