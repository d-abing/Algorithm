from collections import deque
N = int(input())
myQueue = deque()

for i in range(1, N+1):
    myQueue.append(i)
    
while len(myQueue) > 1 :
    myQueue.popleft()
    myQueue.append(myQueue.popleft())
    
print(myQueue[0])