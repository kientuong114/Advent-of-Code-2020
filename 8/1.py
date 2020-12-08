import sys
sys.path.insert(0, '../bootcode')

import timeit
from bootcode.machine import BootcodeMachine

def solution(inp):
    states = set()
    accumulator = 0
    ip = 0
    last_acc = 0
    while True:
        opc, n = inp[ip].split(' ')
        n = int(n)
        if opc == 'nop':
            ip += 1
        elif opc == 'acc':
            accumulator += n
            ip += 1
        elif opc == 'jmp':
            ip += n
        if ip not in states:
            states.add(ip)
            last_acc = accumulator
        else:
            return last_acc

def new_solution(inp):
    bcm = BootcodeMachine(inp)
    bcm.run_until_loop()
    return bcm.accum

if __name__ == "__main__":
    with open('8.in') as f:
        inp = f.readlines()
    inp = [l.strip() for l in inp]
    print(f"old solution: {solution(inp)}")
    print("time for 10k runs:", timeit.timeit('solution(inp)', setup="from __main__ import solution, inp", number=10000))
    print(f"new solution: {new_solution(inp)}")
    print("time for 10k runs:", timeit.timeit('new_solution(inp)', setup="from __main__ import new_solution, inp", number=10000))
