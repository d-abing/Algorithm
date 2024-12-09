N = int(input())

for _ in range(N):
    n = int(input())
    
    if n % 2 == 0:
        print("{} is even".format(n))
    else:
        print("{} is odd".format(n))