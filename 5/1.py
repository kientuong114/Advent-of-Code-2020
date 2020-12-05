import timeit
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
    max_ID = 0
    for seat in inp:
        row, col = seat[:7], seat[7:]
        ID = decoderow(row) * 8 + decodecol(col)
        if max_ID < ID:
            max_ID = ID
    return max_ID

def oneliner(inp):
    return max(int(line.translate(str.maketrans('RLBF', '1010')),2) for line in inp)

if __name__ == "__main__":
    with open('5.in') as f:
        inp = f.readlines()
    inp = [l.strip() for l in inp if l]
    print(f"old solution: {solution(inp)}")
    print("time for 10k runs:", timeit.timeit('solution(inp)', setup="from __main__ import solution, inp", number=100000))
    print(f"one liner: {oneliner(inp)}")
    print("time for 10k runs:", timeit.timeit('oneliner(inp)', setup="from __main__ import oneliner, inp", number=100000))
