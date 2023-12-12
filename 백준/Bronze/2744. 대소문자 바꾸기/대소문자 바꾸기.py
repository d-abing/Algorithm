import sys
ipnut = sys.stdin.readline

S = input()
result = ''

for s in S:
    if s.isupper():
        result += s.lower()
    else:
        result += s.upper()

print(result)