def solution(inp):
    inp.append(0)
    inp = sorted(inp)
    inp.append(max(inp)+3)

    obl = set([0])
    for x, y in zip(inp, inp[1:]):
        if y - x == 3:
            obl.add(x)
            obl.add(y)
    tot = 1
    obl = list(sorted(obl))
    for o, oo in zip(obl, obl[1:]):
        c = inp.index(oo) - inp.index(o) - 1
        if oo - o > 3:
            tot *= 2**c - (oo-o)//3
        else:
            tot *= 2**c
    return tot


if __name__ == "__main__":
    with open('10.in') as f:
        inp = f.readlines()
    inp = [int(l.strip()) for l in inp]
    print(solution(inp))
