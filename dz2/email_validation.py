import re

def fun(s):
    if not s or '@' not in s:
        return False
    parts = s.split('@')
    if len(parts) != 2:
        return False
    username, rest = parts[0], parts[1]
    if not username or not rest or '.' not in rest:
        return False
    idx = rest.rfind('.')
    websitename, extension = rest[:idx], rest[idx+1:]
    if not websitename or not extension or len(extension) > 3:
        return False
    if not re.match(r'^[a-zA-Z0-9_-]+$', username):
        return False
    if not re.match(r'^[a-zA-Z0-9]+$', websitename):
        return False
    if not re.match(r'^[a-zA-Z]+$', extension):
        return False
    return True

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    import sys
    n = int(input())
    if n < 1:
        print("Ошибка: количество адресов должно быть не менее 1", file=sys.stderr)
        sys.exit(1)
    emails = []
    for _ in range(n):
        emails.append(input())
    if any(not e.strip() for e in emails):
        print("Ошибка: пустые значения не допускаются", file=sys.stderr)
        sys.exit(1)
    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)
