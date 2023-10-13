from sys import stdin
input = stdin.readline

N = int(input())
M = int(input())
numbers = list(map(int, input().split()))

count = 0

for i in range(N):
    target_num = M - numbers[i]
    count += numbers[i + 1:].count(target_num)

print(count)
