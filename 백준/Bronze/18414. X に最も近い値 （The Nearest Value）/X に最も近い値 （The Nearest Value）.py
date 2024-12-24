X, L, R = map(int, input().split())
diff = 100000
answer = 0

for i in range(L, R + 1):
    if abs(X - i) < diff:
        answer = i
        diff = X - i
    else:
        break
        
print(answer)