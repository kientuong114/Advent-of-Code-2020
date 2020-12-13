import math

def solution(inp):
    _ = int(inp[0])
    ids = [(idx, int(x)) for idx, x in enumerate(inp[1].split(',')) if x != 'x']
    curr_time, curr_idx = ids[0]
    for idx, x in ids[1:]:
        i = 0
        while True:
            res = (curr_time + curr_idx * i + idx) / x
            if res.is_integer():
                curr_time = int(x * res - idx)
                curr_idx = math.lcm(curr_idx, x)
                break
            i += 1
    return curr_time

if __name__ == "__main__":
    with open('13.in') as f:
        inp = f.readlines()
    inp = [l.strip() for l in inp]
    print(solution(inp))
