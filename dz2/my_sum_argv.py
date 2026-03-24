import sys

if __name__ == '__main__':
    nums = [float(x) for x in sys.argv[1:]]
    s = sum(nums)
    print(int(s) if s == int(s) else s)
