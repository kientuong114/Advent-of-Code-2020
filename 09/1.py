def is_valid(n, preamble):
    for val in preamble:
        if n - val in preamble:
            return True
    return False

def solution(inp):
    preamble = set(inp[:25])
    idx = 25
    while True:
        if not is_valid(inp[idx], preamble):
            return inp[idx]
        preamble.add(inp[idx])
        preamble.remove(inp[idx-25])
        idx += 1
    return None

if __name__ == "__main__":
    with open('9.in') as f:
        inp = f.readlines()
    inp = [int(l.strip()) for l in inp]
    print(solution(inp))
