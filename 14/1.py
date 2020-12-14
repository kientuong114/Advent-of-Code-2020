import re

def apply_mask(val, mask):
    s = 0
    if not mask:
        return val
    for idx, ch in enumerate(reversed(mask)):
        if ch == 'X':
            s += val & (1 << idx)
        else:
            s += int(ch) << idx
    return s

mem_re = re.compile(r'mem\[(\d+)\] = (\d+)')

def solution(inp):
    mem = {}
    mask = None
    for line in inp:
        if line.startswith('mem'):
            m = mem_re.match(line)
            loc, val = int(m.group(1)), int(m.group(2))
            mem[loc] = apply_mask(val, mask)
        else:
            mask = list(line.split(' = ')[1])
    return sum(mem.values())

if __name__ == "__main__":
    with open('14.in') as f:
        inp = f.readlines()
    inp = [l.strip() for l in inp]
    print(solution(inp))
