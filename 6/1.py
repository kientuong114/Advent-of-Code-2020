def solution(inp):
    return sum(len(set(line.replace('\n', ''))) for line in inp)

if __name__ == "__main__":
    with open('6.in') as f:
        inp = f.read().strip().split('\n\n')
    print(solution(inp))
