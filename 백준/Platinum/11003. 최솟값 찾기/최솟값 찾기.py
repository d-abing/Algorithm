from sys import stdin
from collections import deque

input = stdin.readline

N, L = map(int, input().split())
numbers = list(map(int, input().split()))

min_dq = deque()

for i in range(N):
    while len(min_dq) > 0:
        pop_value = min_dq.pop()
        if numbers[i] <= pop_value[1]:
            continue
        else:
            min_dq.append(pop_value)
            break
    min_dq.append([i, numbers[i]])
    if min_dq[0][0] <= i - L:
        min_dq.popleft()
    print(str(min_dq[0][1]), end=" ")
