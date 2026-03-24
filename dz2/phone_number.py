def normalize(phone):
    s = ''.join(c for c in phone if c.isdigit())
    if len(s) == 11 and s[0] in '078':
        s = s[1:]
    if len(s) != 10:
        return None
    return (s, '+7 ({}) {}-{}-{}'.format(s[0:3], s[3:6], s[6:8], s[8:10]))

def wrapper(f):
    def fun(l):
        pairs = []
        for p in l:
            t = normalize(p)
            if t:
                pairs.append(t)
        pairs.sort(key=lambda x: x[0])
        return [x[1] for x in pairs]
    return fun

@wrapper
def sort_phone(l):
    return sorted(l)

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    print(*sort_phone(l), sep='\n')
