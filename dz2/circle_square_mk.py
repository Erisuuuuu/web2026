import random
import math

def circle_square_mk(r, n):
    if n == 0:
        return 0.0
    count = 0
    for _ in range(n):
        x = random.uniform(-r, r)
        y = random.uniform(-r, r)
        if x*x + y*y <= r*r:
            count += 1
    return (2*r)**2 * count / n
