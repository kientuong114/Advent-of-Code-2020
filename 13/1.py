def solution(inp):
    earliest = int(inp[0])
    ids = [(int(x), int(x)*(earliest//int(x) + 1)) for x in inp[1].split(',') if x != 'x']
    r, r1 = min(ids, key=lambda x: x[1])
    return r * (r1 - earliest)

if __name__ == "__main__":
    with open('13.in') as f:
        inp = f.readlines()
    inp = [l.strip() for l in inp]
    print(solution(inp))
