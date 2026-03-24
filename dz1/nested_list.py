import sys
n = int(input())
if not (2 <= n <= 5):
    print("Ошибка: N должно быть от 2 до 5", file=sys.stderr)
    sys.exit(1)
students = []
for _ in range(n):
    name = input()
    score = float(input())
    students.append([name, score])
scores = sorted(set(s[1] for s in students))
second = scores[1]   # вторая по величине снизу (второй минимальный балл)
names = sorted([s[0] for s in students if s[1] == second])
for name in names:
    print(name)
