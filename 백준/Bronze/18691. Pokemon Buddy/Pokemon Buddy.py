T = int(input())
groups = [1, 3, 5]
for _ in range(T):
    G, C, E = map(int, input().split())
    
    if E - C < 0:
        print(0)
    else:
        print((E - C) * groups[G - 1])