import sys
input = sys.stdin.readline

K = int(input())
result = []
for _ in range(K):
    n = int(input())
    if n == 0:
        result.pop()
    else:
        result.append(n)

print(sum(result))