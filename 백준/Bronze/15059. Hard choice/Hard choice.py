Ca, Ba, Pa = map(int, input().split())
Cr, Br, Pr = map(int, input().split())

answer = 0

if Ca - Cr < 0:
    answer += Cr - Ca

if Ba - Br < 0:
    answer += Br - Ba

if Pa - Pr < 0:
    answer += Pr - Pa

print(answer)