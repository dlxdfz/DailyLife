import time
import random
import tqdm

def Gen(n=1000):
    for _ in range(n):
        p1 = random.randint(0, n-1)
        p2 = random.randint(0, n-1)
        yield (p1, p2)

def count(n=1000):
    d = dict([(i, 0) for i in range(n)])
    for p1, p2 in tqdm.tqdm(Gen(n)):
        d[p1] += 1
        d[p2] += 1
    return d

if __name__=="__main__":
    s = time.time()
    d = count(n=7000000)
    e = time.time()
    print(e - s)
