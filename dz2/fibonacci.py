cube = lambda x: x**3

def fibonacci(n):
    if n < 0 or n > 15:
        raise ValueError("Ошибка: n должно быть от 0 до 15")
    if n == 0:
        return []
    if n == 1:
        return [0]
    res = [0, 1]
    for _ in range(2, n):
        res.append(res[-1] + res[-2])
    return res

if __name__ == '__main__':
    import sys
    n = int(input())
    if not (1 <= n <= 15):
        print("Ошибка: n должно быть от 1 до 15", file=sys.stderr)
        sys.exit(1)
    print(list(map(cube, fibonacci(n))))
