K = int(input())

for i in range(1, K + 1):
    answer = 0

    n, s, d = map(int, input().split())
    for _ in range(n):
        di, vi = map(int, input().split())
        if di / s <= d:
            answer += vi

    print("Data Set {}:".format(i))
    print(answer)
    print()