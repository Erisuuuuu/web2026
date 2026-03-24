import timeit

# fact_it быстрее fact_rec при n порядка сотен и выше
def fact_rec(n):
    if n < 0 or n > 10**5:
        raise ValueError("Ошибка: n должно быть от 0 до 10^5")
    if n <= 1:
        return 1
    return n * fact_rec(n - 1)

def fact_it(n):
    if n < 0 or n > 10**5:
        raise ValueError("Ошибка: n должно быть от 0 до 10^5")
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r

if __name__ == '__main__':
    n = 100
    t_rec = timeit.timeit(lambda: fact_rec(n), number=1000)
    t_it = timeit.timeit(lambda: fact_it(n), number=1000)
    print('rec:', t_rec, 'it:', t_it)
