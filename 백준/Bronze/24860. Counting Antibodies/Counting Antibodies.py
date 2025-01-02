Vk, Jk = map(int, input().split())
Vt, Jt = map(int, input().split())
Vh, Dh, Jh = map(int, input().split())

answer = (Vk * Jk) * (Vh * Dh * Jh) + (Vt * Jt) * (Vh * Dh * Jh)
print(answer)