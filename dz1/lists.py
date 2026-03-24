import sys
n = int(input())
if n < 1:
    print("Ошибка: количество команд должно быть не менее 1", file=sys.stderr)
    sys.exit(1)
arr = []
for _ in range(n):
    line = input().split()
    cmd = line[0]
    if cmd == "insert":
        arr.insert(int(line[1]), int(line[2]))
    elif cmd == "print":
        print(arr)
    elif cmd == "remove":
        arr.remove(int(line[1]))
    elif cmd == "append":
        arr.append(int(line[1]))
    elif cmd == "sort":
        arr.sort()
    elif cmd == "pop":
        arr.pop()
    elif cmd == "reverse":
        arr.reverse()



