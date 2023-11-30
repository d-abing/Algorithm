from collections import deque

N, K = map(int, input().split())
queue = deque()

for i in range(1, N + 1):
    queue.append(i)

result = []
order = 1
while queue:
    if order % K != 0:
        queue.append(queue.popleft())
    else:
        result.append(queue.popleft())
    order += 1

print("<", end='')
print(*result, sep=', ', end='')
print(">", end='')