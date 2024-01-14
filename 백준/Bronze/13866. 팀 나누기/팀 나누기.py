ABCD = list(map(int, input().split()))
ABCD.sort()

num1 = ABCD[0] + ABCD[3]
num2 = ABCD[1] + ABCD[2]

print(abs(num1 - num2))