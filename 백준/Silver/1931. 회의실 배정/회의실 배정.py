import sys
input = sys.stdin.readline

N = int(input())
meeting = [tuple(map(int, reversed(input().split()))) for _ in range(N)]

meeting.sort()

time = 0
count = 0
for i in range(N):
    if meeting[i][1] >= time:
        time = meeting[i][0]
        count += 1

print(count)
