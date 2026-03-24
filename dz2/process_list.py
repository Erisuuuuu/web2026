import timeit

def process_list(arr):
    if len(arr) > 10**3:
        raise ValueError("Ошибка: длина списка не более 10^3")
    return [i**2 if i % 2 == 0 else i**3 for i in arr]

def process_list_gen(arr):
    if len(arr) > 10**3:
        raise ValueError("Ошибка: длина списка не более 10^3")
    for i in arr:
        yield i**2 if i % 2 == 0 else i**3

if __name__ == '__main__':
    arr = list(range(1000))
    t1 = timeit.timeit(lambda: process_list(arr), number=5000)
    t2 = timeit.timeit(lambda: list(process_list_gen(arr)), number=5000)
    print('list comp:', t1, 'gen:', t2)
