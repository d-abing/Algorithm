import sys
input = sys.stdin.readline

def print_sign(num):
    if num < 0:
        print('-')
    elif num == 0:
        print(0)
    else:
        print('+')

A = int(input())
print_sign(sum([int(input()) for _ in range(A)]))
B = int(input())
print_sign(sum([int(input()) for _ in range(B)]))
C = int(input())
print_sign(sum([int(input()) for _ in range(C)]))
