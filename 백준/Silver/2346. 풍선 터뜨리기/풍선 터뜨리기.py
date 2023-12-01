import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
deque = deque()
for i in range(2, N + 1):
    deque.append(i)
memos = list(map(int, input().split()))
result = [1]

while deque:
    memo = memos[result[-1] - 1]
    if memo > 0:
        for _ in range(memo - 1):
            deque.append(deque.popleft())
        result.append(deque.popleft())
    else:
        for _ in range(-memo):
            deque.appendleft(deque.pop())
        result.append(deque.popleft())

print(*result)