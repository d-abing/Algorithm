import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
white = 0
blue = 0

def check(A, N):
    global white
    global blue
    if sum(map(sum, A)) == 0:
        white += 1
        return
    elif sum(map(sum, A)) == N * N:
        blue += 1
        return
    else:
        mid = N // 2
        check([row[:mid] for row in A[:mid]], mid) #1
        check([row[mid:] for row in A[:mid]], mid) #2
        check([row[:mid] for row in A[mid:]], mid) #3
        check([row[mid:] for row in A[mid:]], mid) #4

check(A, N)
print(white)
print(blue)