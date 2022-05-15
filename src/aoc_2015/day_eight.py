from pathlib import Path


def count_code_representation(string_literal):
    return len(string_literal)


def count_string_characters(string_literal):
    return len(eval(string_literal))


def code_string_diff(string_literal):
    return count_code_representation(string_literal) - count_string_characters(string_literal)


def count_new_encode_diff(string_literal):
    return 2 + string_literal.count("\\") + string_literal.count('"')


if __name__ == "__main__":
    input_file = Path("./src/aoc_2015/input/day_eight.txt")
    puzzle_input = input_file.open().readlines()
    puzzle_input = [l.strip() for l in puzzle_input]

    print(f"Part 1: {sum(code_string_diff(s) for s in puzzle_input)}")
    print(f"Part 2: {sum(count_new_encode_diff(s) for s in puzzle_input)}")
