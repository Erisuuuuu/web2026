import sys
n = int(input())
if not (2 <= n <= 100):
    print("Ошибка: n должно быть от 2 до 100", file=sys.stderr)
    sys.exit(1)
arr = list(map(int, input().split()))
if len(arr) != n:
    print("Ошибка: ожидается n чисел во второй строке", file=sys.stderr)
    sys.exit(1)
s = sorted(set(arr))

if len(s) >= 2:
    print(s[-2])
else:
    print(s[-1])
