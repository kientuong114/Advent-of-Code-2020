import math

def decoderow(r):
    assert(len(r) == 7)
    bot = 0
    top = 127
    for ch in r:
        if ch == 'F':
            top = (top + bot) // 2
        else:
            bot = math.ceil((top + bot) / 2)
    assert(top == bot)
    return top

def decodecol(r):
    assert(len(r) == 3)
    bot = 0
    top = 7
    for ch in r:
        if ch == 'L':
            top = (top + bot) // 2
        else:
            bot = math.ceil((top + bot) / 2)
    assert(top == bot)
    return top

def solution(inp):
    v = set()
    for seat in inp:
        row, col = seat[:7], seat[7:]
        r = decoderow(row)
        c = decodecol(col)
        v.add(r*8+c)
    for r in range(128):
        for c in range(8):
            if r*8+c not in v and r*8+c+1 in v and r*8+c-1 in v:
                return r*8+c

if __name__ == "__main__":
    with open('5.in') as f:
        inp = f.readlines()
    inp = [l.strip() for l in inp if l]
    print(solution(inp))
