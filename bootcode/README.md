# Bootcode Interpreter

## About

This is an implementation of the Bootcode interpreter for Day 8 (and maybe beyond) of the 2020 edition of [Advent of Code](https://adventofcode.com).

## Usage

To use the interpreter, just import the `BootcodeMachine` object and run it:

```python
program = [
    'nop +0',
    'acc +1',
    'jmp +4',
    'acc +3',
    'jmp -3',
    'acc -99',
    'acc +1',
    'jmp -4',
    'acc +6'
]

bcm = BootcodeMachine(program)
bcm.run_until_loop()
print(bcm.accum)
```

## Testing

To run the unit tests, run:

```
python -m unittest -v
```
