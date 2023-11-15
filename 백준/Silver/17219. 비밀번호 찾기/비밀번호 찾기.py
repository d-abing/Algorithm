import sys
input = sys.stdin.readline

N, M = map(int, input().split())
id_password = {}

for _ in range(N):
    id, password = input().split()
    id_password[id] = password

for _ in range(M):
    print(id_password.get(input()[:-1]))
