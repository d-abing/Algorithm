import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

A.sort()

for i in range(M):
    target = B[i]
    start = 0
    end = N - 1
    has_found = False
    while start <= end:
        middle = (end + start) // 2
        if target < A[middle]:
            end = middle - 1
        elif target > A[middle]:
            start = middle + 1
        else:
            has_found = True
            break
    if has_found:
        print(1)
    else:
        print(0)
