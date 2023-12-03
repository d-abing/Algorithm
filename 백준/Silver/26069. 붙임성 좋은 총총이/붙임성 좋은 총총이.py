import sys
input = sys.stdin.readline

N = int(input())
set = set()

for _ in range(N):
    A, B = input().split()
    if A == 'ChongChong' or B == 'ChongChong':
        set.add(A)
        set.add(B)
    elif A in set or B in set:
        set.add(A)
        set.add(B)

print(len(set))