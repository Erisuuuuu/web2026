def process_list(arr):
    if len(arr) > 10**3:
        raise ValueError("Ошибка: длина списка не более 10^3")
    result = []
    for i in arr:
        if i % 2 == 0:
            result.append(i**2)
        else:
            result.append(i**3)
    return result

