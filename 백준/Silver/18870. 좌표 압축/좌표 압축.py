import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = {}

for i, a in enumerate(dict.fromkeys(sorted(A))):
    if str(a) not in B:
        B[str(a)] = i

for a in A:
    print(B[str(a)], end=' ')
