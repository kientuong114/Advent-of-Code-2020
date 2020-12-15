def solution(inp):
    d = {}
    for idx, n in enumerate(inp[:-1]):
        d[int(n)] = idx+1
    curr_turn = len(inp)
    last_num = int(inp[-1])
    while curr_turn < 30000000:
        if last_num not in d:
            d[last_num] = curr_turn
            last_num = 0
        else:
            prev = last_num
            last_num = curr_turn - d[last_num]
            d[prev] = curr_turn
        curr_turn += 1
    return last_num

if __name__ == "__main__":
    with open('15.in') as f:
        inp = f.read().split(',')
    print(solution(inp))
