def fun(s):
    # your code here
    # return True if s is a valid email, else return False

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
