from collections import deque

def solution(inp):
    d = deque(inp)

    for _ in range(100):
        val = d[0]
        d.rotate(-1)
        x1, x2, x3 = d.popleft(), d.popleft(), d.popleft()

        target = val - 1 or 9
        while target in (x1, x2, x3):
            target -= 1
            if target == 0:
                target = 9

        rot_count = 0
        while True:
            d.rotate(-1)
            rot_count += 1
            if d[-1] == target:
                d.extend([x1, x2, x3])
                break
        d.rotate(rot_count + 3)

    while d[-1] != 1:
        d.rotate(-1)
    d.pop()

    return ''.join(str(l) for l in d)

if __name__ == "__main__":
    with open('23.in') as f:
        inp = [int(l) for l in f.read().strip()]
    print(solution(inp))
