D, H, M = map(int, input().split())

timeDiff = ( D - 11 ) * 24 * 60 + ( H - 11 ) * 60 + ( M - 11 )

if timeDiff < 0:
    print(-1)
else:
    print(timeDiff)