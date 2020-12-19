d = {}

def match(msg, rules):
    global d
    if len(rules) == 0:
        if msg == '':
            return True
        else:
            return False
    rule = d[rules[0]]
    if len(rule) == 1 and rule[0] in ('a', 'b'):
        return msg[0] == rule[0] and match(msg[1:], rules[1:])
    else:
        for or_list in rule:
            new_rules = or_list + rules[1:]
            if match(msg, new_rules):
                return True
        return False

def solution(rules, msg):
    global d
    for rule in rules:
        label, targets = rule.split(': ')
        targets = [t.split(' ') for t in targets.split(' | ')]
        if len(targets) == 1 and targets[0][0] in ('"a"', '"b"'):
            targets = [targets[0][0][1:-1]]
        else:
            targets = [list(map(int, t)) for t in targets]
        d[int(label)] = targets
    return sum(1 for m in msg if match(m, [0]))

if __name__ == "__main__":
    with open('19.in') as f:
        rules, msg = f.read().split('\n\n')
    print(solution(rules.split('\n'), msg.strip().split('\n')))
