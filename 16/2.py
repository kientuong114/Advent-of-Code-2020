def s_to_range(s):
    l,h = s.split('-')
    l = int(l)
    h = int(h)
    return set(range(l,h+1))

def solution(inp):
    classes = {r.split(': ')[0]: list(map(s_to_range, r.split(': ')[1].split(' or '))) for r in inp[0].split('\n')}
    ticks = [list(map(int, t.split(','))) for t in inp[2].split('\n')[1:]]
    err_rate = 0
    valid_ticks = []
    for t in ticks:
        for entry in t:
            found_class = False
            for c in classes.values():
                for p in c:
                    if entry in p:
                        found_class = True
            if not found_class:
                break
        else:
            valid_ticks.append(t)
    class_order = [[] for _ in range(len(classes))]
    for cl_name, cl in classes.items():
        for idx in range(len(classes)):
            for t in valid_ticks:
                if t[idx] not in cl[0] and t[idx] not in cl[1]:
                    break
            else:
                class_order[idx].append(cl_name)
    my_tick = inp[1].split('\n')[1].split(',')
    count = 1
    while True:
        to_delete = None
        for idx, cl in enumerate(class_order):
            if len(cl) == 1:
                if cl[0].startswith('departure'):
                    count *= int(my_tick[idx])
                to_delete = cl[0]
        if not to_delete:
            break
        for cl in class_order:
            if to_delete in cl:
                cl.remove(to_delete)
    return count

if __name__ == "__main__":
    with open('16.in') as f:
        inp = f.read().strip().split('\n\n')
    print(solution(inp))
