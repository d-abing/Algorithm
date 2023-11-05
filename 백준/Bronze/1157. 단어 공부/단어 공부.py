s = input()
upper_s = s.upper()
A = [0] * 26

for s in upper_s:
    A[ord(s) - 65] += 1

if A.count(max(A)) > 1:
    print('?')
else:
    print(chr(A.index(max(A)) + 65))
