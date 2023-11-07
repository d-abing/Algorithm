import math
Min, Max = map(int, input().split())
Check = [False] * (Max - Min + 1)

for i in range(2, int(math.sqrt(Max) + 1)):
    pow = i * i
    start_index = Min // pow
    if Min % pow != 0:
        start_index += 1
    for j in range(start_index, Max // pow + 1):
        Check[int((j * pow) - Min)] = True

count = 0

for i in range(len(Check)):
    if not Check[i]:
        count += 1

print(count)
