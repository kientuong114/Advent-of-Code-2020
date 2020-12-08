import unittest

from bootcode.utils import parse_instruction, patch_program

class TestUtils(unittest.TestCase):
    def test_patching(self):
        program = ['nop +0', 'acc +3', 'jmp -1']
        new_program = patch_program(program, 0, 'jmp', 2)
        self.assertCountEqual(new_program, ['jmp +2', 'acc +3', 'jmp -1'])
        new_program = patch_program(program, 1, 'nop', -1)
        self.assertCountEqual(new_program, ['nop +0', 'nop -1', 'jmp -1'])
        new_program = patch_program(program, 2, 'acc', 4)
        self.assertCountEqual(new_program, ['nop +0', 'acc +3', 'acc +4'])
    def test_parsing(self):
        res = parse_instruction('jmp +3')
        self.assertCountEqual(res, ('jmp', 3))
        res = parse_instruction('nop -1')
        self.assertCountEqual(res, ('nop', -1))
        res = parse_instruction('acc +6')
        self.assertCountEqual(res, ('acc', 6))

if __name__ == "__main__":
    unittest.main()

