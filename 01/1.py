import timeit

def old_solution(nums):
    d = set(nums)
    for l in inp:
        if 2020 - l in d:
            return l * (2020 - l)

def one_liner(nums):
    return next(l*(2020-l) for l in nums if (2020-l) in set(nums))

if __name__ == "__main__":
    with open('1.in') as f:
        inp = f.readlines()
    inp = [int(l.strip()) for l in inp]
    print(f"old solution: {old_solution(inp)}")
    print("time for 10k runs:", timeit.timeit('old_solution(inp)', setup="from __main__ import old_solution, inp", number=10000))
    print(f"one liner: {one_liner(inp)}")
    print("time for 10k runs:", timeit.timeit('one_liner(inp)', setup="from __main__ import one_liner, inp", number=10000))
