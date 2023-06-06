import sys
from collections import deque
input = sys.stdin.readline

N, L = map(int, input().split())
numbers = list(map(int, input().split()))
deque = deque()

for i in range(N):
    while deque and deque[-1][0] > numbers[i]:
        deque.pop()
    deque.append((numbers[i], i))
    if deque[0][1] <= i - L:
        deque.popleft()
    print(deque[0][0], end=" ")