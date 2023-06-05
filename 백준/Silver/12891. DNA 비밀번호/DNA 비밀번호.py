import sys
input = sys.stdin.readline

S, P = map(int, input().split())
str_dna = input().replace("\n", "")
dna = "ACGT"
list_min = list(map(int, input().split()))
dict_min = {}
dict_minus = {}
result = 0

for i in range(len(dna)):
    dict_min[dna[i]] = list_min[i]

def count_bases(string):
    base_count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for base in string:
        if base in base_count:
            base_count[base] += 1
    return base_count

dict_count = count_bases(str_dna[0: P])

for i in dict_min:
    dict_minus[i] = dict_count[i]- dict_min[i]

first_letter = ""

for i in range(S - P + 1):
    first_letter = str_dna[i: i + P][0]
    if not any(value < 0 for value in dict_minus.values()) :
        result += 1
    if i != S - P :
        dict_minus[first_letter] -= 1
        dict_minus[str_dna[P + i]] += 1


print(result)
