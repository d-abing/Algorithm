N, B = map(int, input().split())

numbers = [0] * 36
for i in range(36):
    if i < 10:
        numbers[i] = str(i)
    else:
        numbers[i] = chr(i + 55)

result = ''
while N // B > 0:
    result += numbers[N % B]
    N //= B
result += numbers[N]

print(result[-1:-(len(result) + 1):-1])
