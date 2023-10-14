from sys import stdin

input = stdin.readline

S, P = map(int, input().split())
dna_str = input()
minimums = list(map(int, input().split()))

i = 0
j = P

counts = list()
counts.append(dna_str[i:j].count('A') - minimums[0])
counts.append(dna_str[i:j].count('C') - minimums[1])
counts.append(dna_str[i:j].count('G') - minimums[2])
counts.append(dna_str[i:j].count('T') - minimums[3])

count = 0

while j <= S:
    if counts[0] >= 0 and counts[1] >= 0 and counts[2] >= 0 and counts[3] >= 0:
        count += 1

    if j == S:
        break

    if dna_str[i] == 'A':
        counts[0] -= 1
    elif dna_str[i] == 'C':
        counts[1] -= 1
    elif dna_str[i] == 'G':
        counts[2] -= 1
    elif dna_str[i] == 'T':
        counts[3] -= 1
    i += 1

    if dna_str[j] == 'A':
        counts[0] += 1
    elif dna_str[j] == 'C':
        counts[1] += 1
    elif dna_str[j] == 'G':
        counts[2] += 1
    elif dna_str[j] == 'T':
        counts[3] += 1
    j += 1

print(count)
