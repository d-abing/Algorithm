T = int(input())

for _ in range(T):
    R, S = input().split()
    result = ''
    for s in S:
        for _ in range(int(R)):
            result += s
    print(result)
    