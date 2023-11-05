import sys
input = sys.stdin.readline

N, M = map(int, input().split())
times = list(map(int, input().split()))

start = max(times)
end = sum(times)

while start <= end:
    middle = (start + end) // 2

    tmp_sum = 0
    count = 1
    for i in range(N):
        if tmp_sum + times[i] <= middle:
            tmp_sum += times[i]
        else:
            count += 1
            tmp_sum = times[i]

    if count <= M:
        end = middle - 1
    else:
        start = middle + 1

print(start)
