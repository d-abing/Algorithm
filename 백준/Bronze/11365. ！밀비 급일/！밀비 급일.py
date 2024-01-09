import sys

input = sys.stdin.readline

while True:
    code = input().strip()
    if code == 'END':
        break

    print(code[-1:-(len(code) + 1):-1])