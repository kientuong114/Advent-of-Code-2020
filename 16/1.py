def s_to_range(s):
    l,h = s.split('-')
    l = int(l)
    h = int(h)
    return set(range(l,h+1))

def solution(inp):
    classes = [list(map(s_to_range, r.split(': ')[1].split(' or '))) for r in inp[0].split('\n')]
    ticks = [list(map(int, t.split(','))) for t in inp[2].split('\n')[1:]]
    err_rate = 0
    for t in ticks:
        for entry in t:
            found_class = False
            for c in classes:
                for p in c:
                    if entry in p:
                        found_class = True
            if found_class:
                continue
            else:
                err_rate += entry
                break
    return err_rate

if __name__ == "__main__":
    with open('16.in') as f:
        inp = f.read().strip().split('\n\n')
    print(solution(inp))
