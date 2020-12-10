import sys
sys.path.insert(0, '../bootcode')

import timeit
from bootcode.machine import BootcodeMachine
from bootcode.utils import patch_program, parse_instruction

def execute(inp):
    states = set()
    accumulator = 0
    ip = 0
    while True:
        try:
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
            else:
                return False, 0
        except:
            return True, accumulator

def solution(inp):
    for i in range(len(inp)):
        if inp[i].startswith('nop'):
            res, c = execute(inp[:i] + [inp[i].replace('nop', 'jmp')] + inp[i+1:])
            if res:
                return c
        elif inp[i].startswith('jmp'):
            res, c = execute(inp[:i] + [inp[i].replace('jmp', 'nop')] + inp[i+1:])
            if res:
                return c

def new_solution(inp):
    for idx, line in enumerate(inp):
        opcode, arg = parse_instruction(line)
        if opcode == 'nop':
            new_prog = patch_program(inp, idx, 'jmp', arg)
        elif opcode == 'jmp':
            new_prog = patch_program(inp, idx, 'nop', arg)
        else:
            continue
        bcm = BootcodeMachine(new_prog)
        bcm.run_until_loop()
        if bcm.is_halted:
            return bcm.accum


if __name__ == "__main__":
    with open('8.in') as f:
        inp = f.readlines()
    inp = [l.strip() for l in inp]
    print(f"old solution: {solution(inp)}")
    print(f"new solution: {new_solution(inp)}")
