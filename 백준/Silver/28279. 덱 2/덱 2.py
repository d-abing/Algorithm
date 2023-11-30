import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
deque = deque()

for _ in range(N):
    order = list(map(int, input().split()))
    if order[0] == 1:
        deque.appendleft(order[1])
    if order[0] == 2:
        deque.append(order[1])
    if order[0] == 3:
        if deque:
            print(deque.popleft())
        else:
            print(-1)
    if order[0] == 4:
        if deque:
            print(deque.pop())
        else:
            print(-1)
    if order[0] == 5:
        print(len(deque))
    if order[0] == 6:
        if deque:
            print(0)
        else:
            print(1)
    if order[0] == 7:
        if deque:
            print(deque[0])
        else:
            print(-1)
    if order[0] == 8:
        if deque:
            print(deque[-1])
        else:
            print(-1)