import sys
n, m = map(int, input().split())
if n < 1 or m < 1:
    print("Ошибка: n и m должны быть не менее 1", file=sys.stderr)
    sys.exit(1)
items = []
for _ in range(m):
    parts = input().split()
    cost = int(parts[-1])
    weight = int(parts[-2])
    name = " ".join(parts[:-2])
    items.append((name, weight, cost))

items.sort(key=lambda x: x[2]/x[1], reverse=True)
cap = n
result = []
for name, w, c in items:
    if cap <= 0:
        break
    if w <= cap:
        result.append((name, w, c))
        cap -= w
    else:
        frac = cap / w
        result.append((name, round(cap, 2), round(c * frac, 2)))
        cap = 0

result.sort(key=lambda x: x[2], reverse=True)
for name, w, c in result:
    if isinstance(w, float) or isinstance(c, float):
        print(name, f"{w:.2f}", f"{c:.2f}")
    else:
        print(name, w, c)
