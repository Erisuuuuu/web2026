import operator

def person_lister(f):
    def inner(people):
        people_sorted = sorted(people, key=lambda x: int(x[2]))
        return [f(p) for p in people_sorted]
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    import sys
    n = int(input())
    if not (1 <= n <= 10):
        print("Ошибка: N должно быть от 1 до 10", file=sys.stderr)
        sys.exit(1)
    people = [input().split() for i in range(n)]
    print(*name_format(people), sep='\n')
