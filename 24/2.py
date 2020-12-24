dirs = {
    'e': (1, 1, 0),
    'se': (1, 0, -1),
    'w': (-1, -1, 0),
    'nw': (-1, 0, 1),
    'ne': (0, 1, 1),
    'sw': (0, -1, -1)
}

def nbs(tile):
    return set([(tile[0]+x, tile[1]+y, tile[2]+z) for x,y,z in dirs.values()])

def solution(inp):
    blacks = set()

    for line in inp:
        idx = 0
        prec = None
        seq = []

        while idx < len(line):
            if line[idx] in ('s', 'n'):
                prec = line[idx]
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

    for _ in range(100):
        new_blacks = set()

        all_tiles = set(blacks)
        for t in blacks:
            all_tiles |= nbs(t)

        for tt in all_tiles:
            x = sum(1 for n in nbs(tt) if n in blacks)
            if 1 <= x <= 2 and tt in blacks or tt not in blacks and x == 2:
                new_blacks.add(tt)

        blacks = new_blacks
    return len(blacks)

if __name__ == "__main__":
    with open('24.in') as f:
        inp = f.readlines()
    inp = [l.strip() for l in inp]
    print(solution(inp))
