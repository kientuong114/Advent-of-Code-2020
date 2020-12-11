from collections import Counter

def count_adjacent(mtx, x, y):
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    counter = 0
    for dx, dy in dirs:
        for mult in range(1, len(mtx)):
            new_x = x + mult * dx
            new_y = y + mult * dy
            if new_x in range(len(mtx[0])) and new_y in range(len(mtx)):
                if mtx[new_y][new_x] == '#':
                    counter += 1
                if mtx[new_y][new_x] == '.':
                    continue
                break
            else:
                break
    return counter


def solution(inp):
    while True:
        inp_copy = [list(l) for l in inp]
        for y, line in enumerate(inp):
            for x, ch in enumerate(line):
                if ch == 'L' and count_adjacent(inp, x, y) == 0:
                    inp_copy[y][x] = '#'
                elif ch == '#' and count_adjacent(inp, x, y) >= 5:
                    inp_copy[y][x] = 'L'
        if inp == inp_copy:
            break
        inp = inp_copy
    return sum(Counter(line)['#'] for line in inp)

if __name__ == "__main__":
    with open('11.in') as f:
        inp = f.readlines()
    inp = [list(l.strip()) for l in inp]
    print(solution(inp))
