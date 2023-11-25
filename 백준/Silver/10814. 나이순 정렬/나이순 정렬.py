import sys
from queue import PriorityQueue
input = sys.stdin.readline

N = int(input())
pq = PriorityQueue()
for i in range(N):
    a, b = input().split()
    pq.put((int(a), i, b))

for i in range(N):
    a, i, b = pq.get(i)
    print(a, b)
