from pathlib import Path


def parse_program(program, initial_registers, log=False):
    line_n = 0
    registers = initial_registers
    while line_n >= 0 and line_n < len(program):
        registers, line_n = parse_instruction(line_n, program[line_n], registers, log)
    return registers


def parse_artimetic_instruction(line, registers):
    instruction, register = line.split(" ")
    if instruction == "hlf":
        registers[register] /= 2
    elif instruction == "tpl":
        registers[register] *= 3
    elif instruction == "inc":
        registers[register] += 1
    return registers


def parse_jump(line_n, line, registers):
    instruction_parts = line.split(" ")
    instruction = instruction_parts[0]
    prefix, offset = (
        instruction_parts[-1][0],
        instruction_parts[-1][1:],
    )
    line_jump = int(offset) * (1 if prefix == "+" else -1)
    if instruction == "jmp":
        line_n += line_jump
    else:
        register = instruction_parts[1].replace(",", "")
        if instruction == "jie":
            is_even = registers[register] % 2 == 0
            line_n += line_jump if is_even else 1
        elif instruction == "jio":
            line_n += line_jump if registers[register] == 1 else 1
    return line_n


def parse_instruction(line_n, line, registers, log):
    if log:
        print(f"Line {line_n+1}: {line} {registers} -> | ", end="")
    if line.startswith("j"):
        line_n = parse_jump(line_n, line, registers)
    else:
        line_n += 1
        registers = parse_artimetic_instruction(line, registers)
    if log:
        print(f"{registers} continue at line {line_n+1}")
    return registers, line_n


if __name__ == "__main__":
    puzzle_input = Path("./src/aoc_2015/input/day_twenty_three.txt")
    program = [line.strip() for line in puzzle_input.open().readlines()]
    registers = {"a": 0, "b": 0}
    registers = parse_program(program, registers)
    print(f"Part 1: value in register {registers['b']}")
    registers = {"a": 1, "b": 0}
    registers = parse_program(program, registers)
    print(f"Part 2: value in register {registers['b']}")
