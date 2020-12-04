import re

def solution(inp):
    counter = 0
    for e in inp:
        present = set()
        e = e.split(' ')
        for pair in e:
            entry, val = pair.split(':')
            present.add(entry)
            if entry == 'byr':
                if len(val) != 4:
                    break
                if not 1920 <= int(val) <= 2002:
                    break
            elif entry == 'iyr':
                if len(val) != 4:
                    break
                if not 2010 <= int(val) <= 2020:
                    break
            elif entry == 'eyr':
                if len(val) != 4:
                    break
                if not 2020 <= int(val) <= 2030:
                    break
            elif entry == 'hgt':
                if val[-2:] == 'cm':
                    if not 150 <= int(val[:-2]) <= 193:
                        break
                elif val[-2:] == 'in':
                    if not 59 <= int(val[:-2]) <= 76:
                        break
                else:
                    break
            elif entry == 'hcl':
                if len(val) != 7:
                    break
                if not re.match('#[a-f0-9]{6}', val):
                    break
            elif entry == 'ecl':
                if val != 'amb' and val != 'blu' and val != 'brn' and val != 'gry' and val != 'grn' and val != 'hzl' and val != 'oth':
                    break
            elif entry == 'pid':
                if len(val) != 9:
                    break
                if not re.match('\d{9}', val):
                    break
        else:
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
