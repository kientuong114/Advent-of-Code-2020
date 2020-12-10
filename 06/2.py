from functools import reduce

def solution(inp):
    count = 0
    for line in inp:
        line = line.split('\n')
        inter = set(line[0])
        for elem in line[1:]:
            inter = inter.intersection(set(elem))
        count += len(inter)
    return count

def oneliner(inp):
    return sum(len(reduce(lambda x, y: set(x).intersection(set(y)), line.split('\n'))) for line in inp)

if __name__ == "__main__":
    with open('6.in') as f:
        inp = f.read().strip().split('\n\n')
    print(solution(inp))
    print(oneliner(inp))
