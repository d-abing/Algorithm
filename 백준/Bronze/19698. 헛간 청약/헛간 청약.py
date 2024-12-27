N, W, H, L = map(int, input().split())

answer = min(N, (W // L) * (H // L))
print(answer)