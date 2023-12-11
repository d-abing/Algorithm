import sys
input = sys.stdin.readline

T = int(input())

# a층의 b호에 살려면 자신의 아래층의 1호부터 b호까지의 사람들의 수의 합만큼
# 사람들을 데려와 살아야 한다.

for _ in range(T):
    k = int(input()) #층
    n = int(input()) #호

    apartment = [[] for _ in range(k + 1)]
    apartment[0] = [i for i in range(1, n + 1)]

    for i in range(1, k + 1):
        for j in range(n):
            apartment[i].append(sum(apartment[i - 1][:j + 1]))

    print(apartment[k][n - 1])