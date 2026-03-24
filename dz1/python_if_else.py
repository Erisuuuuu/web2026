import sys
n = int(input())
if not (1 <= n <= 100):
    print("Ошибка: n должно быть от 1 до 100", file=sys.stderr)
    sys.exit(1)
if n % 2 != 0:
    print("Weird")
else:
    if (2 <= n <= 5) or (n > 20):
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
