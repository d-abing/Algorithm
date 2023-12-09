import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]
D = [0] * (N + 1)
D[0] = -1
times = [0] * (N + 1)

for i in range(1, N + 1):
    tmp = list(map(int, input().split()))
    time = tmp[0]
    times[i] = time
    pre = tmp[1:-1]
    for j in pre:
        graph[j].append(i)
    D[i] += len(pre)

queue = deque()

queue = deque()
for i in range(1, N + 1):
    if D[i] == 0:
        queue.append(i)

result = [0] * (N + 1)

while queue:
    out = queue.popleft()
    for i in graph[out]:
        D[i] -= 1
        result[i] = max(result[i], result[out] + times[out])
        if D[i] == 0:
            queue.append(i)

for i in range(1, N + 1):
    result[i] += times[i]

print(*result[1:], sep='\n')