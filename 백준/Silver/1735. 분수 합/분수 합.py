A, B = map(int, input().split())
C, D = map(int, input().split())

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

E = (A * D) + (B * C)
F = B * D

print(E // gcd(E, F), F // gcd(E, F))