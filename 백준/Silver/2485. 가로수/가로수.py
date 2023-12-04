import sys
input = sys.stdin.readline

N = int(input())
trees = [int(input()) for _ in range(N)]
start = trees[0]
for i in range(N):
    trees[i] -= start
end = trees[-1]

def gcd(a, b):
	if b == 0:
		return a
	else:
		return gcd(b, a % b)

for i in range(2, N):
	trees[i] = gcd(trees[i], trees[i - 1])

print(end // trees[-1] + 1 - N)
