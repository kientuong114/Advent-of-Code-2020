import unittest

from .utils import open_program
from bootcode.machine import BootcodeMachine, HaltedException

class TestException(unittest.TestCase):
    def test_halting_exception(self):
        program = open_program('programs/day8_example_patched.in')
        mac = BootcodeMachine(program)
        mac.execute()
        self.assertTrue(mac.is_halted)
        self.assertRaises(HaltedException, mac.execute_step)
        self.assertRaises(HaltedException, mac.execute)
        self.assertRaises(HaltedException, mac.run_until_loop)


if __name__ == "__main__":
    unittest.main()

