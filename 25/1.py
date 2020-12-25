import tqdm

def solution(inp):
    t = int(inp[1])
    x = 0
    for i in tqdm.tqdm(range(20201227)):
        if pow(7, i, 20201227) == t:
            x = i
            break
    return pow(int(inp[0]), x, 20201227)

if __name__ == "__main__":
    with open('25.in') as f:
        inp = f.readlines()
    print(solution(inp))
