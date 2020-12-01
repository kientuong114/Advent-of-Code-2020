if __name__ == "__main__":
    with open('1.in') as f:
        inp = f.readlines()
    inp = [int(l.strip()) for l in inp]
    d = set()
    for l in inp:
        if 2020 - l in d:
            n1 = l
            n2 = 2020 - l
            print(n1 * n2)
            break
        else:
            d.add(l)
