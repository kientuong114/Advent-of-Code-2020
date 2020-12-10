def solution(inp):
    bgs = {}
    for line in inp:
        bag, lst = line.strip('.').split(' contain ')
        lst = lst.split(', ')
        bag = bag[:-1]
        for b in lst:
            num, b = b.split(' ', 1)
            if b.endswith('s'):
                b = b[:-1]
            if b not in bgs:
                bgs.update({b: [bag]})
            else:
                bgs[b].append(bag)
    visited = set()
    Q = ['shiny gold bag']
    counter = 0
    while Q:
        v = Q.pop(0)
        if v in visited:
            continue
        visited.add(v)
        counter += 1
        if v not in bgs:
            continue
        for n in bgs[v]:
            if n not in visited:
                Q.append(n)
    return counter - 1

if __name__ == "__main__":
    with open('7.in') as f:
        inp = f.readlines()
    inp = [l.strip() for l in inp]
    print(solution(inp))
