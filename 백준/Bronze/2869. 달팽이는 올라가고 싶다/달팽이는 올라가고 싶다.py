A, B, V = map(int, input().split())

sum = (V - A) // (A - B) + 1

if (V - A) % (A - B) > 0:
    sum += 1

print(sum)
        