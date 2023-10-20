import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    result = 1
    for i in range(1, N + 1):
        result *= (M - i + 1)
        result //= i
    print(result)
