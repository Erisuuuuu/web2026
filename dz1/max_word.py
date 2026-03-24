with open("example.txt", "r", encoding="utf-8") as f:
    text = f.read()

def clean_word(w):
    res = []
    for c in w:
        if c.isalpha():
            res.append(c)
    return "".join(res)

words = text.split()
max_len = 0
seen = []
for w in words:
    cw = clean_word(w)
    if not cw:
        continue
    L = len(cw)
    if L > max_len:
        max_len = L
        seen = [cw]
    elif L == max_len and cw not in seen:
        seen.append(cw)

order = []
seen_set = set()
for w in words:
    cw = clean_word(w)
    if len(cw) == max_len and cw not in seen_set:
        order.append(cw)
        seen_set.add(cw)

for w in order:
    print(w)
