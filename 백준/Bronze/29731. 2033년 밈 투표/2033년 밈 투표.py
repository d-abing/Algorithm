promise = [
    "Never gonna give you up",
    "Never gonna let you down",
    "Never gonna run around and desert you",
    "Never gonna make you cry",
    "Never gonna say goodbye",
    "Never gonna tell a lie and hurt you",
    "Never gonna stop"
]

N = int(input())
changed = False
for _ in range(N):
    if input().rstrip() not in promise:
        changed = True
        break

if changed:
    print("Yes")
else:
    print("No")