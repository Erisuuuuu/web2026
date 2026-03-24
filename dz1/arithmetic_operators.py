import sys
a = int(input())
b = int(input())
if not (0 <= a <= 10**10 and 0 <= b <= 10**10):
    print("Ошибка: a и b должны быть от 0 до 10^10", file=sys.stderr)
    sys.exit(1)
print(a + b)
print(a - b)
print(a * b)
