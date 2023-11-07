import sys
input = sys.stdin.readline

max_value = 0
x, y = 1, 1
for i in range(9):
    numbers = list(map(int, input().split()))
    if max(numbers) > max_value:
        max_value = max(numbers)
        x, y = i + 1, numbers.index(max(numbers)) + 1

print(max_value)
print(x, y)
