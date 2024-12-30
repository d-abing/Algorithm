t1, m1, t2, m2 = map(int, input().split())

if t2 < t1 or (t2 == t1 and m2 < m1):
    t2 += 24
if m2 < m1:
    m2 += 60
    t2 -= 1

times = (t2 - t1) * 60 + (m2 - m1)
count = times // 30

print(times, count)