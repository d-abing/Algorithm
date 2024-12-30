S = int(input())
A = int(input())
B = int(input())
icecream_price = 250

if S <= A:
    print(icecream_price)
else:
    icecream_price += ((S - A) // B) * 100
    if (S - A) % B != 0:
        icecream_price += 100
    print(icecream_price)