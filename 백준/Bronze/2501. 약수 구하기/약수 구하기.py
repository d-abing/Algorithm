N, K = map(int, input().split())
count = 0
i = 1
while i < N + 1:
    if N % i == 0:
        count += 1
        if count == K:
            break
    i += 1
    
if count < K:
    i = 0

print(i)
