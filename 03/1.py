import timeit

def solution(inp):
    counter = 0
    x, y = 0, 0
    while y != len(inp):
        if inp[y][x] == '#':
            counter += 1
        y += 1
        x += 3
        x %= len(inp[0])
    return counter

def oneliner(inp):
    return sum(1 for idx, row in enumerate(inp) if row[idx*3 % len(inp[0])] == '#')

if __name__ == "__main__":
    with open('3.in') as f:
        inp = f.readlines()
    inp = [l.strip() for l in inp]
    print(f"old solution: {solution(inp)}")
    print("time for 10k runs:", timeit.timeit('solution(inp)', setup="from __main__ import solution, inp", number=10000))
    print(f"one liner: {oneliner(inp)}")
    print("time for 10k runs:", timeit.timeit('oneliner(inp)', setup="from __main__ import oneliner, inp", number=10000))
