count = 0
start = 0
for _ in range(8):
    line = input()
    for i in range(start, 8, 2):
        if line[i] == 'F':
            count += 1
    start = 1 if start == 0 else 0
print(count)