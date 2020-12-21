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
                maycontain[cc] &= ing
            else:
                maycontain[cc] = set(ing)

    discard = set.union(*maycontain.values())

    return sum(len(ing.difference(discard)) for ing, _ in ll)

if __name__ == "__main__":
    with open('21.in') as f:
        inp = f.readlines()
    inp = [l.strip() for l in inp]
    print(solution(inp))
