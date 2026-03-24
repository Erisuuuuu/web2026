def compute_average_scores(scores):
    if not scores or not scores[0]:
        raise ValueError("Ошибка: список оценок не пустой, 0 < N,X ≤ 100")
    x, n = len(scores), len(scores[0])
    if not (0 < n <= 100 and 0 < x <= 100):
        raise ValueError("Ошибка: 0 < N ≤ 100, 0 < X ≤ 100")
    result = []
    for i in range(n):
        s = sum(t[i] for t in scores)
        result.append(round(s / len(scores), 1))
    return tuple(result)

if __name__ == '__main__':
    import sys
    n, x = map(int, input().split())
    if not (0 < n <= 100 and 0 < x <= 100):
        print("Ошибка: N и X от 1 до 100", file=sys.stderr)
        sys.exit(1)
    scores = [tuple(map(float, input().split())) for _ in range(x)]
    for v in compute_average_scores(scores):
        print(v)
