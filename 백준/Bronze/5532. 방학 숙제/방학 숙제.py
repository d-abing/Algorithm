import sys
input = sys.stdin.readline

L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

day = 0
while A > 0 or B > 0:
    day += 1
    A -= C
    B -= D

print(L - day)