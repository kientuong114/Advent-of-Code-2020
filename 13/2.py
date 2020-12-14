import math
#from sage.all import *

def solution(inp):
    _ = int(inp[0])
    ids = [(idx, int(x)) for idx, x in enumerate(inp[1].split(',')) if x != 'x']
    curr_time, curr_idx = ids[0]
    for idx, x in ids[1:]:
        i = 0
        while True:
            res = (curr_time + curr_idx * i + idx) / x
            if res.is_integer():
                curr_time = int(x * res - idx)
                curr_idx = math.lcm(curr_idx, x)
                break
            i += 1
    return curr_time

def oneliner(inp): #This is kinda cheating lul
    #from sage.arith.misc import CRT
    #Uncomment the line above and the line on the top to import sage
    return lambda x: CRT(list(x[0]), list(x[1]))(list(zip(*[(-x, int(y)) for x, y in enumerate(inp[1].split(',')) if y != 'x'])))

if __name__ == "__main__":
    with open('13.in') as f:
        inp = f.readlines()
    inp = [l.strip() for l in inp]
    print(solution(inp))
    print(oneliner(inp))
