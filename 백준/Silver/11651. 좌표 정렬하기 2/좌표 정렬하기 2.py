import sys
from queue import PriorityQueue
input = sys.stdin.readline

N = int(input())
pq = PriorityQueue()
for _ in range(N):
    a, b = map(int, input().split())
    pq.put((b, a))

for i in range(N):
    b, a = pq.get(i)
    print(a, b)
