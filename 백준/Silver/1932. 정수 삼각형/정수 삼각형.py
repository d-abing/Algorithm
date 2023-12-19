import sys
input = sys.stdin.readline

n = int(input())
triangle = []
result = []
for _ in range(n):
    floor = list(map(int, input().split()))
    triangle.append(floor)
    result.append([0] * len(floor))

result[0] = [triangle[0][0]]

index = 0
for i in range(n - 1):
    for j in range(len(triangle[i])):
        for k in range(2):
            if triangle[i + 1][j + k] + triangle[i][j] > result[i + 1][j + k]:
                result[i + 1][j + k] = triangle[i + 1][j + k] + triangle[i][j]
    triangle[i + 1] = result[i + 1]

print(max(result[n - 1]))