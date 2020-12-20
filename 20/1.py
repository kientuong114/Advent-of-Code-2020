d = {}

def solution(inp):
    global d
    for til in inp:
        til = til.split('\n')
        num, tile = til[0], til[1:]
        num = int(num.split(' ')[1].strip(':'))
        d[num] = {
            'T': tuple(tile[0]),
            'B': tuple(tile[-1] if tile[-1] else tile[-2]),
            'R': tuple(l[-1] for l in tile if l),
            'L': tuple(l[0] for l in tile if l)
        }
    for n, til in d.items():
        for nn, tt in d.items():
            if n == nn:
                continue
            for direc in ('T', 'B', 'L', 'R'):
                if til[direc] == tt['T']:
                    d[n]['N'+direc] = (nn, 'T', False)
                elif til[direc] == tt['B']:
                    d[n]['N'+direc] = (nn, 'B', False)
                elif til[direc] == tt['L']:
                    d[n]['N'+direc] = (nn, 'L', False)
                elif til[direc] == tt['R']:
                    d[n]['N'+direc] = (nn, 'R', False)
                elif tuple(reversed(til[direc])) == tt['T']:
                    d[n]['N'+direc] = (nn, 'T', True)
                elif tuple(reversed(til[direc])) == tt['B']:
                    d[n]['N'+direc] = (nn, 'B', True)
                elif tuple(reversed(til[direc])) == tt['L']:
                    d[n]['N'+direc] = (nn, 'L', True)
                elif tuple(reversed(til[direc])) == tt['R']:
                    d[n]['N'+direc] = (nn, 'R', True)
    count = 1
    for n, til in d.items():
        if 'NL' in til and 'NR' in til and not 'NB' in til and not 'NT' in til:
            count *= n
        if 'NL' in til and 'NR' not in til and 'NB' in til and 'NT' not in til:
            count *= n
        if 'NL' not in til and 'NR' in til and 'NB' in til and not 'NT' in til:
            count *= n
        if 'NL' in til and 'NR' not in til and not 'NB' in til and 'NT' in til:
            count *= n
        if 'NL' not in til and 'NR' in til and not 'NB' in til and 'NT' in til:
            count *= n
        if 'NL' not in til and 'NR' not in til and 'NB' in til and 'NT' in til:
            count *= n
    return count

if __name__ == "__main__":
    with open('20.in') as f:
        inp = f.read().split('\n\n')
    print(solution(inp))
