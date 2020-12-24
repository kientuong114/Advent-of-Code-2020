dirs = {
    'e': (1, 1, 0),
    'se': (1, 0, -1),
    'w': (-1, -1, 0),
    'nw': (-1, 0, 1),
    'ne': (0, 1, 1),
    'sw': (0, -1, -1)
}

def solution(inp):
    blacks = set()
    for line in inp:
        idx = 0
        prec = None
        seq = []
        while idx < len(line):
            if line[idx] in ('s', 'n'):
                prec = line[idx]
                idx += 1
            else:
                seq.append(dirs[(prec if prec else '') + line[idx]])
                prec = None
                idx += 1
        pos = (0, 0, 0)
        for dx, dy, dz in seq:
            pos = (pos[0]+dx, pos[1]+dy, pos[2]+dz)
        if pos in blacks:
            blacks.remove(pos)
        else:
            blacks.add(pos)
    return len(blacks)

if __name__ == "__main__":
    with open('24.in') as f:
        inp = f.readlines()
    inp = [l.strip() for l in inp]
    print(solution(inp))
