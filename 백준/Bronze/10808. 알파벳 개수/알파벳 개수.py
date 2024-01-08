import sys
input = sys.stdin.readline

S = input().strip()
A = [0 for _ in range(26)]

for s in S:
    A[ord(s) - 97] += 1

print(*A)