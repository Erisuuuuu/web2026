import os
import sys

if __name__ == '__main__':
    path = sys.argv[1]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    files.sort(key=lambda f: (os.path.splitext(f)[1], f))
    for f in files:
        print(f)
