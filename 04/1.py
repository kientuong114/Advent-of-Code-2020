def solution(inp):
    counter = 0
    for entry in inp:
        tags = set()
        entry = entry.split(' ')
        for pair in entry:
            tag, _ = pair.split(':')
            tags.add(tag)
        tags.add('cid')                 #Adds if not already present, otherwise does nothing
        if len(tags) == 8:
            counter += 1
    return counter

if __name__ == "__main__":
    with open('4.in') as f:
        inp = f.read()
    inp = [l.strip().replace('\n', ' ') for l in inp.split('\n\n')]
    inp = [l for l in inp if l]
    print(solution(inp))
