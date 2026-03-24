n = int(input())
pairs = []
for _ in range(n):
    ai, bi = map(int, input().split())
    pairs.append((ai, bi))
t = int(input())
count = 0
for ai, bi in pairs:
    if ai <= t <= bi:
        count += 1
print(count)
