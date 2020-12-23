from collections import deque
import tqdm

class Node:
    def __init__(self, v):
        self.r = None
        self.v = v
    def __repr__(self):
        return f'<Node: value={self.v}, right={self.r.v}>'

def print_list(d):
    cursor = d[1]
    while True:
        print(cursor.v, end=', ')
        cursor = cursor.r
        if cursor.v == 1:
            break

def solution(inp):
    d = {}

    prec = None
    for i in inp + list(range(10, 1000001)):
        n = Node(i)
        if prec:
            prec.r = n
        prec = n
        d[i] = n

    cursor = d[inp[0]]
    prec.r = cursor

    for i in tqdm.tqdm(range(10000000)):
        val = cursor.v
        x1 = cursor.r
        x2 = x1.r
        x3 = x2.r
        cursor.r = x3.r

        target = val - 1 or 1000000
        while target in (x1.v, x2.v, x3.v):
            target -= 1
            if target == 0:
                target = 1000000

        insert_pt = d[target]
        x3.r = insert_pt.r
        insert_pt.r = x1
        cursor = cursor.r

    return d[1].r.v * d[1].r.r.v

if __name__ == "__main__":
    with open('23.in') as f:
        inp = [int(l) for l in f.read().strip()]
    print(solution(inp))
