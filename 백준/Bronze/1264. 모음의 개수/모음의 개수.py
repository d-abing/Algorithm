import sys
input = sys.stdin.readline
A = 'aeiou'
while True:
    s = input()[:-1].lower()
    if s == '#':
        break

    count = 0
    for a in A:
        count += s.count(a)

    print(count)