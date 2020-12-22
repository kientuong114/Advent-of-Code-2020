from collections import deque

def solution(inp):
    p1, p2 = inp
    p1 = deque([int(l) for l in p1.splitlines()[1:]])
    p2 = deque([int(l) for l in p2.splitlines()[1:]])

    while len(p1) and len(p2):
        p1c, p2c = p1.popleft(), p2.popleft()
        if p1c > p2c:
            p1.extend([p1c, p2c])
        else:
            p2.extend([p2c, p1c])

    p = p1 if len(p1) else p2

    return sum((i+1)*x for i, x in enumerate(reversed(p)))

if __name__ == "__main__":
    with open('22.in') as f:
        inp = f.read().strip().split('\n\n')
    print(solution(inp))
