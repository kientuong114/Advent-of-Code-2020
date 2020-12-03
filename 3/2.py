import timeit

def solution(inp):
    ds = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    tot_counter = 1
    for dx, dy in ds:
        counter = 0
        x, y = 0, 0
        while y < len(inp):
            if inp[y][x] == '#':
                counter += 1
            y += dy
            x += dx
            x %= len(inp[0])
        tot_counter *= counter
    return tot_counter

def oneliner(inp):
    from functools import reduce
    return reduce(lambda x,y: x*y, [sum(1 for idx, row in enumerate(inp) if row[(idx//dy)*dx % len(inp[0])] == '#' and idx % dy == 0) for dx, dy in ((1,1), (3,1), (5,1), (7,1), (1,2))])

if __name__ == "__main__":
    with open('3.in') as f:
        inp = f.readlines()
    inp = [l.strip() for l in inp]
    print(f"old solution: {solution(inp)}")
    print("time for 10k runs:", timeit.timeit('solution(inp)', setup="from __main__ import solution, inp", number=10000))
    print(f"one liner: {oneliner(inp)}")
    print("time for 10k runs:", timeit.timeit('oneliner(inp)', setup="from __main__ import oneliner, inp", number=10000))
