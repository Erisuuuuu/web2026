import sys
s = input()
if not (0 < len(s) <= 1000):
    print("Ошибка: длина строки от 1 до 1000", file=sys.stderr)
    sys.exit(1)
res = []
for c in s:
    if c.isupper():
        res.append(c.lower())
    elif c.islower():
        res.append(c.upper())
    else:
        res.append(c)
print("".join(res))
