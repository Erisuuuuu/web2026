import sys
s = input()
if not (0 < len(s) <= 10**6):
    print("Ошибка: длина строки от 1 до 10^6", file=sys.stderr)
    sys.exit(1)
vowels = "AEIOU"
kevin = 0
stuart = 0
n = len(s)

# Перебираем все подстроки: начало i, конец j (подстрока s[i:j])
# За каждую такую подстроку даём 1 очко Кевину (если с гласной) или Стюарту (если с согласной)
for i in range(n):
    for j in range(i + 1, n + 1):
        if s[i] in vowels:
            kevin += 1
        else:
            stuart += 1

if stuart > kevin:
    print("Стюарт", stuart)
elif kevin > stuart:
    print("Кевин", kevin)
else:
    print("Ничья")
