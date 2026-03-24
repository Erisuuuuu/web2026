import sys
n, m = map(int, input().split())
if not (1 <= n <= 10**5 and 1 <= m <= 10**5):
    print("Ошибка: n и m от 1 до 10^5", file=sys.stderr)
    sys.exit(1)
arr = list(map(int, input().split()))
if len(arr) != n:
    print("Ошибка: ожидается n чисел в массиве", file=sys.stderr)
    sys.exit(1)
A = set(map(int, input().split()))
B = set(map(int, input().split()))
if len(A) != m or len(B) != m:
    print("Ошибка: в множествах A и B по m чисел", file=sys.stderr)
    sys.exit(1)
for x in arr + list(A) + list(B):
    if not (1 <= x <= 10**9):
        print("Ошибка: элементы от 1 до 10^9", file=sys.stderr)
        sys.exit(1)
mood = 0
for i in arr:
    if i in A:
        mood += 1
    elif i in B:
        mood -= 1
print(mood)
