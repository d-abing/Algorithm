import sys
from queue import PriorityQueue

input = sys.stdin.readline

N = int(input())
pq = PriorityQueue()
sum = 0

for i in range(N):
    for j, length in enumerate(list(map(ord, list(input().rstrip())))):
        if length != 48:
            if 65 <= length <= 90:
                pq.put((length - 38, i, j))
                sum += length - 38
            else:
                pq.put((length - 96, i, j))
                sum += length - 96

union_find_list = [i for i in range(N + 1)]


def union(a, b):
    a = find(a)
    b = find(b)
    union_find_list[a] = b


def find(num):
    if union_find_list[num] != num:
        union_find_list[num] = find(union_find_list[num])
        return union_find_list[num]
    else:
        return num


result = 0
linked_edge = 0
while linked_edge < N - 1 and pq.qsize() > 0:
    c, a, b = pq.get()
    if find(a) != find(b):
        union(a, b)
        result += c
        linked_edge += 1

if linked_edge == N - 1:
    print(sum - result)
else:
    print(-1)