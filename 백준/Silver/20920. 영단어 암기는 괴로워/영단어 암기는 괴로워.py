import sys
from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())
word_counts = defaultdict(int)

for _ in range(N):
    word = input().rstrip()
    if len(word) >= M:
        word_counts[word] += 1

sorted_list = sorted(word_counts.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for e in sorted_list:
    print(e[0])
