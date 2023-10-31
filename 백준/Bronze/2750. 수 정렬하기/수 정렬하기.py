from sys import stdin
input = stdin.readline

N = int(input())
numbers = [int(input()) for _ in range(N)]

for i in range(N - 1):
    for j in range(N - 1 - i):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(*numbers, sep="\n")