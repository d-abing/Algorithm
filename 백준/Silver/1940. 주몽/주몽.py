from sys import stdin
input = stdin.readline

N = int(input())
M = int(input())
materials = list(map(int, input().split()))
result = 0

for i in range(N - 1):
    if (M - materials[i]) in materials[i + 1:]:
        result += 1

print(result)