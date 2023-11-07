N, B = input().split()
B = int(B)

numbers = [0] * 36
for i in range(36):
    if i < 10:
        numbers[i] = str(i)
    else:
        numbers[i] = chr(i + 55)
        
result = 0

for i in range(-1, -(len(N) + 1), -1):
    result += numbers.index(N[i]) * (B ** (-i - 1))

print(result)