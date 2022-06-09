from atexit import register
import pytest

from aoc_2015.day_twenty_three import parse_instruction, parse_program

instructions_cases = [
    pytest.param({"a": 2}, "hlf a", {"a": 1}),
    pytest.param({"a": 2}, "tpl a", {"a": 6}),
    pytest.param({"a": 2}, "inc a", {"a": 3}),
]

jump_cases = [
    pytest.param(
        {"a": 2},
        [
            "jmp +2",
            "inc a",
            "tpl a",
            "inc a",
        ],
        {"a": 7},
    ),
    pytest.param(
        {"a": 9},
        [
            "jmp +2",
            "jmp +3",
            "inc a",
            "jmp -2",
        ],
        {"a": 10},
    ),
    pytest.param(
        {"a": 2},
        [
            "jie a, +2",
            "inc a",
            "tpl a",
            "inc a",
        ],
        {"a": 7},
    ),
    pytest.param(
        {"a": 1},
        [
            "jio a, +2",
            "inc a",
            "tpl a",
            "inc a",
        ],
        {"a": 4},
    ),
]


@pytest.mark.parametrize("initial_registers,line,expected_registers", instructions_cases)
def test_instructions(initial_registers, line, expected_registers):
    # Act
    actual_registers, _ = parse_instruction(0, line, initial_registers)
    # Assert
    assert expected_registers == actual_registers


@pytest.mark.parametrize("initial_registers,lines,expected_registers", jump_cases)
def test_jumps(initial_registers, lines, expected_registers):
    # Act
    actual_registers = parse_program(lines, initial_registers)
    # Assert
    assert expected_registers == actual_registers
