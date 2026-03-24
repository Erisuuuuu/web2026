import sys
n = int(input())
if not (1 <= n <= 20):
    print("Ошибка: n должно быть от 1 до 20", file=sys.stderr)
    sys.exit(1)
for i in range(n):
    print(i * i)
