a = int(input())
x = int(input())
b = int(input())
y = int(input())
T = int(input())

a_price = a + (T - 30) * x * 21 if T - 30 >= 0 else a
b_price = b + (T - 45) * y * 21 if T - 45 >= 0 else b

print(a_price, b_price)