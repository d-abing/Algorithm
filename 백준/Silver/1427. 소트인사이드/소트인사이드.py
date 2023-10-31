import sys
input = sys.stdin.readline

numbers = list(input())
length = len(numbers)

for i in range(length - 1):
    max_index = numbers[i:].index(max(numbers[i:])) + i
    numbers[i], numbers[max_index] = numbers[max_index], numbers[i]

print(*numbers, sep="")
