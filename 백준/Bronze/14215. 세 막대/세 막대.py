lengths = list(map(int, input().split()))
lengths.sort()
lengths[2] = lengths[0] + lengths[1] - 1 if lengths[2] >= lengths[0] + lengths[1] else lengths[2]
print(sum(lengths))