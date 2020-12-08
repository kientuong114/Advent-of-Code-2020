from typing import List, Tuple

def parse_instruction(instr: str) -> Tuple[str, int]:
    """Parses a Bootcode instruction

    Given a Bootcode instruction in the form of a string, it will return a tuple containing
    the opcode and the argument of the instruction
    """

    opcode, arg = instr.split(' ')
    arg = int(arg)
    return opcode, arg

def patch_program(program: List[str], addr: int, new_opcode: str, new_arg: int):
    """Patches a program at a given address

    Given a Bootcode program in the form of a list of strings, it will return a new program
    with the instruction at `addr` changed to be the one provided.
    """

    return program[:addr] + [f'{new_opcode} {new_arg:+}'] + program[addr+1:]



