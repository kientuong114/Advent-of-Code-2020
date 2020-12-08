def nop(mac: 'BootcodeMachine', arg: int):
    mac.instr_ptr += 1

def jmp(mac: 'BootcodeMachine', arg: int):
    mac.instr_ptr += arg

def acc(mac: 'BootcodeMachine', arg: int):
    mac.instr_ptr += 1
    mac.accum += arg

instr_table = {
    'nop': nop,
    'jmp': jmp,
    'acc': acc
}
