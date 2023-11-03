import sys
input = sys.stdin.readline

numbers = [int(input()) for _ in range(9)]
max_value = max(numbers)
print(max_value)
print(numbers.index(max_value) + 1)
