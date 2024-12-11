p1, q1, p2, q2 = map(int, input().split())
size = (p1 * p2) / (q1 * q2 * 2)

if int(size) == size:
    print(1)
else:
    print(0)