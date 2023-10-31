import sys
input = sys.stdin.readline

N, K, L = map(int, input().split())
round = 1

while True:
    K_even = True if K % 2 == 0 else False
    L_even = True if L % 2 == 0 else False
    if (K_even and not L_even and K - 1 == L) or \
            (L_even and not K_even and L - 1 == K):
        break

    if K_even:
        K = K // 2
    else:
        K = (K + 1) // 2

    if L_even:
        L = L // 2
    else:
        L = (L + 1) // 2

    round += 1

print(round)
