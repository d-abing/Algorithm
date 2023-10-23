from sys import stdin
input = stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
sorted_numbers = numbers.copy()
sorted_numbers.sort()
answer = [0] * N

index = -1
value = 0

for i in range(N):
    if value != sorted_numbers[i]:
        index = -1
    target_index = numbers[index + 1:].index(sorted_numbers[i])
    index = target_index if index == -1 else target_index + index + 1
    value = sorted_numbers[i]
    answer[index] = i

print(*answer, sep = " ")
