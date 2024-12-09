Z = int(input())

for _ in range(Z):
    W, K = map(int, input().split())
    
    if W * K < 2:
        print(0)
    else:
        print(W * K // 2)