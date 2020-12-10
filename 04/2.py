import re

def height(h):
    val, unit = h[:-2], h[-2:]
    if unit == 'cm':
        return 150 <= int(val) <= 193
    elif unit == 'in':
        return 59 <= int(val) <= 76
    else:
        return False

color_re = re.compile(r'#[a-f0-9]{6}')
pid_re = re.compile(r'[0-9]{9}')

validate = {
    'byr': lambda x: 1920 <= int(x) <= 2002,
    'iyr': lambda x: 2010 <= int(x) <= 2020,
    'eyr': lambda x: 2020 <= int(x) <= 2030,
    'hgt': lambda x: height(x),
    'hcl': lambda x: True if color_re.fullmatch(x) else False,
    'ecl': lambda x: x in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
    'pid': lambda x: True if pid_re.fullmatch(x) else False,
    'cid': lambda x: True
}

def solution(inp):
    counter = 0
    for entry in inp:
        tags = set()
        entry = entry.split(' ')
        for pair in entry:
            tag, val = pair.split(':')
            tags.add(tag)
            if not validate[tag](val):
                break
        else:
            tags.add('cid')
            if len(tags) == 8:
                counter += 1
    return counter

if __name__ == "__main__":
    with open('4.in') as f:
        inp = f.read()
    inp = [l.strip().replace('\n', ' ') for l in inp.split('\n\n')]
    inp = [l for l in inp if l]
    print(solution(inp))
