from operator import itemgetter
import re
import itertools

contains_re = re.compile(r'(.*)(\(.*\))')

def solution(inp):
    ll = []
    maycontain = {}

    for line in inp:
        m = contains_re.match(line)
        ingredients, contains = set(m.group(1).split(' ')[:-1]), set(m.group(2)[10:-1].split(', '))
        ll.append((ingredients, contains))

    for ing, cont in ll:
        for cc in cont:
            if cc in maycontain:
                maycontain[cc] = maycontain[cc].intersection(ing)
            else:
                maycontain[cc] = set(ing)

    while any(len(v) > 1 for v in maycontain.values()):
        for k, v in maycontain.items():
            if len(v) == 1:
                for k1 in maycontain.keys():
                    if k1 != k:
                        maycontain[k1] -= v

    mm = {list(v)[0]: k for k, v in maycontain.items()}

    return ','.join(sorted(mm.keys(), key=lambda x: mm[x]))

if __name__ == "__main__":
    with open('21.in') as f:
        inp = f.readlines()
    inp = [l.strip() for l in inp]
    print(solution(inp))
