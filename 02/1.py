
def solution(inp):
    counter = 0
    for l in inp:
        lhs, rhs = l
        times, ch = lhs.split(' ')
        min_t, max_t = times.split('-')
        min_t = int(min_t)
        max_t = int(max_t)
        if min_t <= list(rhs).count(ch) <= max_t:
            counter += 1
    return counter


if __name__ == "__main__":
    with open('2.in') as f:
        inp = f.readlines()
    #inp = [l.strip() for l in inp]
    #inp = [int(l.strip()) for l in inp]
    inp = [l.strip().split(':') for l in inp]
    print(solution(inp))
