c4, a3, a4 = map(int, input().split())

answer = c4 * (0.229 * 0.324) * 2  + a3 * (0.297 * 0.420) * 2  + a4 * (0.210 * 0.297)
print(answer)