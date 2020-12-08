import unittest

from .utils import open_program
from bootcode.machine import BootcodeMachine
from bootcode.utils import parse_instruction, patch_program

class TestHalting(unittest.TestCase):
    def test_halting(self):
        program = open_program('programs/day8.in')
        mac = BootcodeMachine(program)
        mac.run_until_loop()
        self.assertEqual(mac.accum, 1137)

    def test_patched_halting(self):
        program = open_program('programs/day8.in')
        for idx, instr in enumerate(program):
            opcode, arg = parse_instruction(instr)
            if opcode == 'jmp':
                new_prog = patch_program(program, idx, 'nop', arg)
            elif opcode == 'nop':
                new_prog = patch_program(program, idx, 'jmp', arg)
            else:
                continue
            mac = BootcodeMachine(new_prog)
            mac.run_until_loop()
            if mac.is_halted:
                self.assertEqual(mac.accum, 1125)


if __name__ == "__main__":
    unittest.main()
