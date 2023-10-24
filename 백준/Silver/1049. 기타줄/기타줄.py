import sys
input = sys.stdin.readline


N, M = map(int, input().split())

package = []
piece = []

for i in range(M):
    package_price, piece_price = map(int, input().split())
    package.append(package_price)
    piece.append(piece_price)

min_package_price = min(package)
min_piece_price = min(piece)

if min_package_price > (min_piece_price * 6):
    min_package_price = (min_piece_price * 6)

package_count = N // 6
piece_count = N % 6

if (piece_count * min_piece_price) > min_package_price:
    piece_count = 0
    package_count += 1

result = (package_count * min_package_price) + (piece_count * min_piece_price)

print(result)
