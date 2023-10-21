from queue import PriorityQueue
import sys

input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
myQueue = PriorityQueue()

for i in range(N):
    num = int(input())
    if num == 0:
        if myQueue.empty():
            print('0\n')
        else:
            temp = myQueue.get()
            print(str((temp[1])) + '\n')
    else:
        myQueue.put((abs(num), num))
