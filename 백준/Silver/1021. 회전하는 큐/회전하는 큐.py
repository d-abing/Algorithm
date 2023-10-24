from sys import stdin
from collections import deque

input = stdin.readline

N, M = map(int, input().split())
targets = list(map(int, input().split()))

deque = deque()

for i in range(1, N + 1):
    deque.append(i)

count = 0

for i in range(M):
    target = targets[i]
    move_left = False
    if deque.index(target) <= len(deque) // 2:
        move_left = True
    while deque[0] != target:
        if move_left:
            deque.append(deque.popleft())
            count += 1
        else:
            deque.appendleft(deque.pop())
            count += 1
    deque.popleft()

print(count)
