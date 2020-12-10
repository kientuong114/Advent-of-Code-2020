def solution(inp):
    counter = 0
    for l in inp:
        lhs, rhs = l
        times, ch = lhs.split(' ')
        min_t, max_t = times.split('-')
        min_t = int(min_t)
        max_t = int(max_t)
        if rhs[min_t] == ch and not rhs[max_t] == ch or rhs[max_t] == ch and not rhs[min_t] == ch:
            counter += 1
    return counter


if __name__ == "__main__":
    with open('2.in') as f:
        inp = f.readlines()
    inp = [l.strip().split(':') for l in inp]
    print(solution(inp))
