from collections import deque


def play_game(p1, p2):
    p1 = deque(p1)
    p2 = deque(p2)
    state = set()

    while len(p1) and len(p2):
        p1c, p2c = p1.popleft(), p2.popleft()
        res = None
        if p1c <= len(p1) and p2c <= len(p2):
            res, _ = play_game(list(p1)[:p1c], list(p2)[:p2c])

        if not res and p1c > p2c or res == 1:
            p1.extend([p1c, p2c])
        else:
            p2.extend([p2c, p1c])

        t = tuple(p1)
        if t in state:
            return 1, p1
        else:
            state.add(t)

    if len(p1):
        return 1, p1
    else:
        return 2, p2


def solution(inp):
    p1, p2 = inp
    p1 = [int(l) for l in p1.splitlines()[1:]]
    p2 = [int(l) for l in p2.splitlines()[1:]]
    _, p = play_game(p1, p2)
    return sum((i+1)*x for i, x in enumerate(reversed(p)))


if __name__ == "__main__":
    with open('22.in') as f:
        inp = f.read().strip().split('\n\n')
    print(solution(inp))
