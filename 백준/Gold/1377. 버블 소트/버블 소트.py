import sys
input = sys.stdin.readline

N = int(input())
numbers = [(int(input()), i) for i in range(N)]

sorted_numbers = sorted(numbers)

swap_count = 0

for i in range(N):
    swap_count = sorted_numbers[i][1] - i if sorted_numbers[i][1] - i > swap_count else swap_count

swap_count += 1

print(swap_count)
