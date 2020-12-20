from operator import itemgetter
from collections import Counter
import itertools
import re

TILE_HEIGHT = 10 - 2

d = {}

def yield_rotation_flips(tile):
    orig = tile
    for rot in range(4):
        for fl in (False, True):
            tile = orig
            if fl:
                tile = flip(tile)
            for _ in range(rot):
                tile = rotate(tile)
            yield tile

def rotate(t):
    tile = [''.join(reversed(l)) for l in zip(*t['tile'])]
    res = {
        'T': ''.join(reversed(t['L'])),
        'R': t['T'],
        'B': ''.join(reversed(t['R'])),
        'L': t['B']
    }
    nbr_dict = t['nbrs']
    c = {}
    if 'T' in nbr_dict:
        c['R'] = nbr_dict['T']
    if 'R' in nbr_dict:
        c['B'] = nbr_dict['R']
    if 'B' in nbr_dict:
        c['L'] = nbr_dict['B']
    if 'L' in nbr_dict:
        c['T'] = nbr_dict['L']
    res.update({'tile': tile, 'nbrs': c})
    return res

def flip(t):
    tile = [''.join(reversed(l)) for l in t['tile']]
    res = {
        'T': ''.join(reversed(t['T'])),
        'R': t['L'], 
        'B': ''.join(reversed(t['B'])),
        'L': t['R']
    }
    nbr_dict = t['nbrs']
    c = {}
    if 'T' in nbr_dict:
        c['T'] = nbr_dict['T']
    if 'B' in nbr_dict:
        c['B'] = nbr_dict['B']
    if 'R' in nbr_dict:
        c['L'] = nbr_dict['R']
    if 'L' in nbr_dict:
        c['R'] = nbr_dict['L']
    res.update({'tile': tile, 'nbrs': c})
    return res

def find_neighbour_below(t):
    nbr = d[t['nbrs']['B']]
    y = yield_rotation_flips(nbr)
    nbr = next(y)
    idx = 0
    while(t['B'] != nbr['T']):
        nbr = next(y)
        idx += 1
    return nbr

def find_neighbour_right(t):
    nbr = d[t['nbrs']['R']]
    y = yield_rotation_flips(nbr)
    nbr = next(y)
    while(t['R'] != nbr['L']):
        nbr = next(y)
    return nbr

def strip_sides(t):
    return [l[1:-1] for l in t['tile'][1:-1]]

def rotate_flip_img(img, rot, flip):
    if flip:
        img = [''.join(reversed(l)) for l in img]
    for _ in range(rot):
        img = [''.join(reversed(l)) for l in zip(*img)]
    return img


def solution(inp):
    global d
    for til in inp:
        til = til.strip().split('\n')
        num, tile = til[0], til[1:]
        num = int(num.split(' ')[1].strip(':'))
        d[num] = {
            'tile': tile,
            'T': tile[0],
            'B': tile[-1],
            'R': ''.join(l[-1] for l in tile if l),
            'L': ''.join(l[0] for l in tile if l),
            'nbrs': {}
        }

    for n, til in d.items():
        for nn, tt in d.items():
            if n == nn:
                continue
            for direc_n, direc_nn in itertools.product('TBLR', 'TBLR'):
                if til[direc_n] == tt[direc_nn] or til[direc_n] == ''.join(reversed(tt[direc_nn])):
                    d[n]['nbrs'].update({direc_n: nn})

    corners = set()
    for n, til in d.items():
        if len(d[n]['nbrs']) == 2:
            corners.add(n)

    image_tiles = {}

    start = list(corners)[0]

    while 'T' in d[start]['nbrs'] or 'L' in d[start]['nbrs']:
        d[start] = rotate(d[start])

    image_tiles[(0,0)] = d[start]

    for y in range(1, 12):
        image_tiles[(0, y)] = find_neighbour_below(image_tiles[(0, y-1)])
    for y in range(12):
        for x in range(1, 12):
            image_tiles[(x, y)] = find_neighbour_right(image_tiles[(x-1, y)])

    final_img = []

    for r in range(12):
        final_img += strip_sides(image_tiles[(0, r)])
        for c in range(1, 12):
            tile = strip_sides(image_tiles[(c,r)])
            for i in range(TILE_HEIGHT):
                final_img[TILE_HEIGHT*r + i] += tile[i]

    top_line = re.compile('..................#.')
    mid_line = re.compile('#....##....##....###')
    bot_line = re.compile('.#..#..#..#..#..#...')

    n_monsters = 0

    for rot in range(4):
        for flip in (True, False):
            img = rotate_flip_img(final_img, rot, flip)
            for row1, row2, row3 in zip(img, img[1:], img[2:]):
                starts_top = set()
                starts_mid = set()
                starts_bot = set()
                for i in range(len(row1)):
                    ss = top_line.search(row1, i)
                    if ss:
                        starts_top.add(ss.start(0))
                for i in range(len(row2)):
                    ss = mid_line.search(row2, i)
                    if ss:
                        starts_mid.add(ss.start(0))
                for i in range(len(row3)):
                    ss = bot_line.search(row3, i)
                    if ss:
                        starts_bot.add(ss.start(0))
                n_monsters += len(starts_top.intersection(starts_mid).intersection(starts_bot))

    hash_count = 0
    for l in final_img:
        hash_count += Counter(l)['#']
    return hash_count - n_monsters * 15

if __name__ == "__main__":
    with open('20.in') as f:
        inp = f.read().split('\n\n')
    print(solution(inp))
