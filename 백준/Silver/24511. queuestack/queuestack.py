import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
queuestack = list(map(int, input().split()))
queuestack_e = list(map(int, input().split()))

M = int(input())
C = list(map(int, input().split()))
index = []
deque = deque()

for i, queueorstack in enumerate(queuestack):
    if queueorstack == 0:
        deque.append(queuestack_e[i])

for c in C:
    deque.appendleft(c)
    print(deque.pop(), end=' ')
    