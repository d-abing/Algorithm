a, b, c, d, e, f = map(int, input().split())

y = (c * d - a * f) // (b * d - a * e)

if a != 0:
    x = (c - b * y) // a
else:
    x = (f - e * y) // d

print(x, y)