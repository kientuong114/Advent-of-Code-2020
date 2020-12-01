import timeit 

def old_solution(nums):
    d = set(nums)
    for s, l in enumerate(inp):
        for l1 in inp[s:]:
            if 2020 - l - l1 in d:
                return l * l1 * (2020 - l - l1)

def one_liner(nums):
    return next(l*l1*(2020-l-l1) for s, l in enumerate(nums) for l1 in nums[s:] if (2020-l-l1) in set(nums))

if __name__ == "__main__":
    with open('1.in') as f:
        inp = f.readlines()
    inp = [int(l.strip()) for l in inp]
    print(f"old solution: {old_solution(inp)}")
    print("time for 10k runs:", timeit.timeit('old_solution(inp)', setup="from __main__ import old_solution, inp", number=10000))
    print(f"one liner: {one_liner(inp)}")
    print("time for 10k runs:", timeit.timeit('one_liner(inp)', setup="from __main__ import one_liner, inp", number=10000))
