A, B = map(int, input().split())


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print((A * B) // gcd(A, B))
