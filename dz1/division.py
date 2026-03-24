import sys
a = int(input())
b = int(input())
if not (0 <= a <= 10**10 and 0 <= b <= 10**10):
    print("Ошибка: a и b от 0 до 10^10", file=sys.stderr)
    sys.exit(1)
if b == 0:
    print(0)
    print(0.0)
else:
    print(a // b)
    print(a / b)
