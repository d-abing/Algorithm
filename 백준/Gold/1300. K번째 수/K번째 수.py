import sys

input = sys.stdin.readline

N = int(input())
k = int(input())

start = 1
end = k

while start <= end:
    middle = (start + end) // 2
    sum_low_numbers = 0

    for i in range(1, N + 1):
        low_numbers_count = min(middle // i, N)
        sum_low_numbers += low_numbers_count

    if sum_low_numbers < k:
        start = middle + 1
    else:
        end = middle - 1

print(start)
