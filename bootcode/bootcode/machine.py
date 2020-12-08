import logging
from typing import List, Tuple

from bootcode.instructions import instr_table
import bootcode.utils as utils

logger = logging.getLogger(__name__)


class HaltedException(Exception):
    """
    Exception raised when attempting to restart a Bootcode Machine that has halted
    """
    def __init__(self,):
        super().__init__("Attempt to restart a halted Bootcode Machine")


class BootcodeMachine:
    def __init__(self, program: List[str]):
        self.program = program
        self.accum = 0
        self.instr_ptr = 0
        self.n_steps = 0
        self.is_halted = False


    def execute(self, n_steps:int = -1):
        """Begins execution of the Bootcode Machine.

        Each step of execution will execute a single instruction and the state `self`
        will be modified accordingly.
        If `n_steps` is provided, it will run for at most `n_steps` steps of execution.
        Otherwise, it will run until halt, if it ever will.

        Params:
            n_steps: The number of steps for which, at most, the machine will run.
        """

        if n_steps == -1:
            condition = lambda: True
        else:
            condition = lambda: self.n_steps < n_steps

        while condition:
            logger.debug(self)
            self.execute_step()
            if self.is_halted:
                break


    def execute_step(self):
        """Executes one step of the Bootcode Machine.

        Will execute a single instruction and modify the state of the `self` accordingly.
        """

        if self.is_halted:
            raise HaltedException()

        opcode, arg = utils.parse_instruction(self.program[self.instr_ptr])
        instr_table[opcode](self, arg)
        self.n_steps += 1
        if self.instr_ptr < 0 or self.instr_ptr >= len(self.program):
            self.is_halted = True


    def run_until_loop(self):
        """Executes the Bootcode Machine until a loop is detected.

        Will execute the Bootcode Machine until either a loop is detected or the machine halts,
        whichever comes first.
        """

        states = set([0])
        logger.debug(self)
        while True:
            self.execute_step()
            logger.debug(self)
            if self.instr_ptr in states:
                break
            else:
                states.add(self.instr_ptr)
            if self.is_halted:
                break


    def __repr__(self):
        return f"<BootcodeMachine object; accum={self.accum}, instr_ptr={self.instr_ptr}, n_steps={self.n_steps}>"
