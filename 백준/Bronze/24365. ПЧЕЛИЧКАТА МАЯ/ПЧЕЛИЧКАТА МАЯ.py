A, B, C = map(int, input().split())
avg = (A + B + C) // 3
answer = 0

if B <= avg:
    answer = avg - B + (avg - A) * 2
else:
    answer = (B - avg) + (C - avg) * 2

print(answer)