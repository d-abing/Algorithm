import sys
input = sys.stdin.readline

S = input()

for i in range(97, 122 + 1):
    print(S.find(chr(i)), end=' ')
