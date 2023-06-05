from sys import stdin
input = stdin.readline

N = int(input())

result = 1
min_start_num = 0
max_start_num = (N + 1) // 2
sum = 0
minus_value = 1
plus_value = 0

if N > 1:
    for i in range(max_start_num):
        if i * (i + 1) // 2 < N:
            min_start_num = i + 1
            sum = min_start_num * (min_start_num + 1) // 2
            plus_value = min_start_num + 1
        else:
            break

    while plus_value <= max_start_num + 1:
        if sum == N:
            result += 1
            sum -= minus_value
            minus_value += 1
        elif sum < N:
            sum += plus_value
            plus_value += 1
        else:
            sum -= minus_value
            minus_value += 1

print(result)