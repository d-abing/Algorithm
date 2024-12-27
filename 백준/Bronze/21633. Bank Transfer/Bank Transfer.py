k = int(input())

if 100 <= 25 + (k / 100) <= 2000:
    print("{:.2f}".format(25 + (k / 100)))
elif 100 > 25 + (k / 100):
    print("{:.2f}".format(100))
else:
    print("{:.2f}".format(2000))