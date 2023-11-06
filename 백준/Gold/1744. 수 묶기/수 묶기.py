import sys
from queue import PriorityQueue
input = sys.stdin.readline

N = int(input())
plus = PriorityQueue()
one = PriorityQueue()
zero = PriorityQueue()
minus = PriorityQueue()
for _ in range(N):
    data = int(input())
    if data > 1:
        plus.put(-data)
    elif data == 1:
        one.put(data)
    elif data == 0:
        zero.put(data)
    else:
        minus.put(data)

result = 0
while plus.qsize() >= 2:
    result += plus.get() * plus.get()

if plus.qsize() > 0:
    result -= plus.get()

result += one.qsize()

while minus.qsize() >= 2:
    result += minus.get() * minus.get()

if minus.qsize() > 0:
    if zero.qsize() == 0:
        result += minus.get()

print(result)
