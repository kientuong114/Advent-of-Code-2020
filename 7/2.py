from functools import cache

bgs = {}

@cache
def get_count(bag):
    if bag not in bgs:
        return 1
    else:
        counter = 1
        for c, b in bgs[bag]:
            counter += int(c) * get_count(b)
        return counter

def solution(inp):
    global bgs
    for line in inp:
        bag, lst = line.strip('.').split(' contain ')
        lst = lst.split(', ')
        bag = bag[:-1]
        for b in lst:
            num, b = b.split(' ', 1)
            if num == 'no':
                continue
            if b.endswith('s'):
                b = b[:-1]
            if bag not in bgs:
                bgs.update({bag: [(num, b)]})
            else:
                bgs[bag].append((num, b))
    return get_count('shiny gold bag') - 1

if __name__ == "__main__":
    with open('7.in') as f:
        inp = f.readlines()
    inp = [l.strip() for l in inp]
    print(solution(inp))
