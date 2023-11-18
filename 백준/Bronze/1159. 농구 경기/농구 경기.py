import sys
input = sys.stdin.readline

N = int(input())
alpha = [0 for _ in range(27)]

for _ in range(N):
    alpha[ord(input()[:1]) - 97] += 1

predaja = True
for i, a in enumerate(alpha):
    if a >= 5:
        predaja = False
        print(chr(i + 97), end='')

if predaja:
    print("PREDAJA")