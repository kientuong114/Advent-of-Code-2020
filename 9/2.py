target = 133015568

def solution(inp):
    low, high = 0, 1
    ss = inp[low] + inp[high]
    while True:
        if ss < target:
            high += 1
            ss += inp[high]
        elif ss > target:
            ss -= inp[low]
            low += 1
        else:
            l = inp[low:high+1]
            return min(l) + max(l)


if __name__ == "__main__":
    with open('9.in') as f:
        inp = f.readlines()
    inp = [int(l.strip()) for l in inp]
    print(solution(inp))
