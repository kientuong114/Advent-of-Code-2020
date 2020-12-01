if __name__ == "__main__":
    with open('1.in') as f:
        inp = f.readlines()
    inp = [int(l.strip()) for l in inp]
    d = set()
    for s, l in enumerate(inp):
        for l1 in inp[s:]:
            if 2020 - l - l1 in d:
                n1 = l
                n2 = l1
                n3 = 2020 - l - l1
                print(n1 * n2 * n3)
                break
            else:
                d.add(l)

