from collections import Counter

def solution(inp):
    inp.append(0)
    inp = sorted(inp)
    inp.append(max(inp)+3)
    c = Counter([y-x for x,y in zip(inp, inp[1:])])
    return c[3] * c[1]

if __name__ == "__main__":
    with open('10.in') as f:
        inp = f.readlines()
    inp = [int(l.strip()) for l in inp]
    print(solution(inp))
