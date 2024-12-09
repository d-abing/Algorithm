N = int(input())

for _ in range(N):
    test = list(map(int, input().split()))

    tester = test[0]
    c1, c2, c3 = test[1:4]

    if (((c1 / 35) * 100) < 30
            or ((c2 / 30) * 100) < 30
            or ((c3 / 40) * 100) < 30
            or c1 + c2 + c3 < 55):
        print("{} {} FAIL".format(tester, c1 + c2 + c3))
    else:
        print("{} {} PASS".format(tester, c1 + c2 + c3))