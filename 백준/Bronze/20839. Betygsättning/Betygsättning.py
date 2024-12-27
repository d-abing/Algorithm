x, y, z = map(int, input().split())
xx, yy, zz = map(int, input().split())

if zz >= z and yy >= y and xx >= x:
    print("A")
elif zz >= z and yy >= y and xx >= (x / 2):
    print("B")
elif zz >= z and yy >= y:
    print("C")
elif zz >= z and yy >= (y / 2):
    print("D")
elif zz >= z:
    print("E")
