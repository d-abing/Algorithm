N = int(input())

for _ in range(N):
    X, Y = map(int, input().split())
    
    for _ in range(Y):
        print("X" * X)
    
    print()