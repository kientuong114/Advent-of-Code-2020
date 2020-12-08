def open_program(filename: str):
    with open(filename) as f:
        program = f.read().splitlines()
    return program
