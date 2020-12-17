from operator import itemgetter
import itertools

dirs = [coord for coord in itertools.product(range(-1, 2), range(-1, 2), range(-1, 2), range(-1, 2)) if coord != (0,0,0,0)]

def nbs(mtx, loc):
    return sum(1 for d in dirs if (loc[0] + d[0], loc[1] + d[1], loc[2] + d[2], loc[3] + d[3]) in mtx)


def get_range(idx, mtx):
    return range(min(mtx, key=itemgetter(idx))[idx] - 1,
        max(mtx, key=itemgetter(idx))[idx] + 2)


def solution(inp):
    mtx = set()

    for y, line in enumerate(inp):
        for x, ch in enumerate(line):
            if ch == '#':
                mtx.add((x, y, 0, 0))

    for _ in range(6):
        mtx_copy = set()
        range_x = get_range(0, mtx)
        range_y = get_range(1, mtx)
        range_z = get_range(2, mtx)
        range_t = get_range(3, mtx)
        for coord in itertools.product(range_x, range_y, range_z, range_t):
            if coord in mtx:
                if nbs(mtx, coord) in (2, 3):
                    mtx_copy.add(coord)
            else:
                if nbs(mtx, coord) == 3:
                    mtx_copy.add(coord)
        mtx = mtx_copy

    return len(mtx)

if __name__ == "__main__":
    with open('17.in') as f:
        inp = f.readlines()
    inp = [list(l.strip()) for l in inp]
    print(solution(inp))
