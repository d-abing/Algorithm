import sys
from queue import PriorityQueue
input = sys.stdin.readline

N = int(input())
queue = PriorityQueue()
for _ in range(N):
    queue.put(int(input()))

count = 0

while queue.qsize() > 1:
    tmp_sum = 0
    for _ in range(2):
        tmp_sum += queue.get()
    queue.put(tmp_sum)
    count += tmp_sum

print(count)
