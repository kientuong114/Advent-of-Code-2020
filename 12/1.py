drct_to_vct = {
    'N': lambda c,a: (c, complex(0, 1) * a),
    'W': lambda c,a: (c, complex(-1, 0) * a),
    'E': lambda c,a: (c, complex(1, 0) * a),
    'S': lambda c,a: (c, complex(0, -1) * a),
    'F': lambda c,a: (c, c * a),
    'L': lambda c,a: (rot[(rot.index(c) - a//90) % 4], complex(0, 0)),
    'R': lambda c,a: (rot[(rot.index(c) + a//90) % 4], complex(0, 0))
}

rot = [complex(0, 1), complex(1, 0), complex(0, -1), complex(-1, 0)]

def solution(inp):
    acc = complex(0, 0)
    curr_dir = complex(1, 0)
    for lin in inp:
        drct, amt = lin[0], int(lin[1:])
        curr_dir, delta = drct_to_vct[drct](curr_dir, amt)
        acc += delta

    return int(abs(acc.real) + abs(acc.imag))

if __name__ == "__main__":
    with open('12.in') as f:
        inp = f.readlines()
    inp = [l.strip() for l in inp]
    print(solution(inp))
