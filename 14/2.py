import re

def apply_mask_addr(loc, mask):
    if not mask:
        return [loc]
    locs = []
    base = 0
    for idx, ch in enumerate(reversed(mask)):
        if ch == 'X':
            locs.append(idx)
        elif ch == '0':
            base += loc & (1 << idx)
        elif ch == '1':
            base += int(ch) << idx
    addrs = [base]
    for l in locs:
        new_addrs = []
        for a in addrs:
            for v in (0, 1):
                new_addrs.append(a + (v << l))
        addrs = new_addrs
    return addrs

mem_re = re.compile(r'mem\[(\d+)\] = (\d+)')

def solution(inp):
    mem = {}
    mask = None
    for line in inp:
        if line.startswith('mem'):
            m = mem_re.match(line)
            loc, val = int(m.group(1)), int(m.group(2))
            locs = apply_mask_addr(loc, mask)
            for l in locs:
                mem[l] = val
        else:
            mask = list(line.split(' = ')[1])
    return sum(mem.values())

if __name__ == "__main__":
    with open('14.in') as f:
        inp = f.readlines()
    inp = [l.strip() for l in inp]
    print(solution(inp))
