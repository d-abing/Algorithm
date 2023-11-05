s = input()
croatia_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
continue_index = 0
count = 0

for i in range(len(s)):
    if i < continue_index:
        continue
    for j in range(2, 4):
        if s[i:i + j] in croatia_alphabet:
            continue_index = i + j
            break
    count += 1

print(count)
