import math
import cmath

def rect(phase):
    phase = phase % 360
    if phase == 0:
        return complex(1, 0)
    elif phase == 90:
        return complex(0, 1)
    elif phase == 180:
        return complex(-1, 0)
    elif phase == 270:
        return complex(0, -1)

drct_to_vct = {
    'N': lambda w, c, a: (w + complex(0, 1) * a, c),
    'W': lambda w, c, a: (w + complex(-1, 0) * a, c),
    'E': lambda w, c, a: (w + complex(1, 0) * a, c),
    'S': lambda w, c, a: (w + complex(0, -1) * a, c),
    'F': lambda w, c, a: (w, c + w * a),
    'L': lambda w, c, a: (w * rect(a), c),
    'R': lambda w, c, a: (w * rect(-a), c)
}

rot = [complex(0, 1), complex(1, 0), complex(0, -1), complex(-1, 0)]


def solution(inp):
    acc = complex(0, 0)
    curr_dir = complex(1, 0)
    waypoint = complex(10, 1)
    for lin in inp:
        drct, amt = lin[0], int(lin[1:])
        waypoint, acc = drct_to_vct[drct](waypoint, acc, amt)
    return int(abs(acc.real) + abs(acc.imag))

if __name__ == "__main__":
    with open('12.in') as f:
        inp = f.readlines()
    inp = [l.strip() for l in inp]
    print(solution(inp))
