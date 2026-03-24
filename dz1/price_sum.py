with open("products.csv", "r", encoding="utf-8") as f:
    lines = f.readlines()

header = lines[0].strip().split(",")
adult_i = header.index("Взрослый")
pension_i = header.index("Пенсионер")
child_i = header.index("Ребенок")

s_adult = 0.0
s_pension = 0.0
s_child = 0.0

required_len = max(adult_i, pension_i, child_i) + 1

for line in lines[1:]:
    parts = line.strip().split(",")
    if len(parts) >= required_len:
        s_adult += float(parts[adult_i])
        s_pension += float(parts[pension_i])
        s_child += float(parts[child_i])

print(round(s_adult, 2), round(s_pension, 2), round(s_child, 2))
