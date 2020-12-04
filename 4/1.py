def solution(inp):
    counter = 0
    for e in inp:
        present = set()
        e = e.split(' ')
        for pair in e:
            entry, val = pair.split(':')
            if entry not in present:
                present.add(entry)
        if 'byr' not in present or 'iyr' not in present or 'eyr' not in present or 'hgt' not in present or 'hcl' not in present or 'ecl' not in present or 'pid' not in present:
            pass
        else:
            counter += 1
    return counter

if __name__ == "__main__":
    with open('4.in') as f:
        inp = f.read()
    inp = [l.strip().replace('\n', ' ') for l in inp.split('\n\n')]
    inp = [l for l in inp if l]
    print(solution(inp))
