import sys
input = sys.stdin.readline

N = int(input())

count = N

for _ in range(N):
    S = input()
    for i, s in enumerate(S):
        if s in S[:i] and i - S[:i].rindex(s) > 1:
            count -= 1
            break

print(count)
