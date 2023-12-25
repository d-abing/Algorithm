a, b = map(int, input().split())

if (a + b) % 2 == 0:
    n1 = (a + b) // 2
    n2 = a - n1
    
    if n1 >= 0 and n2 >= 0:
        print(n1, n2)
    else:
        print(-1)
else:
    print(-1)
