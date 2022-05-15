from pathlib import Path
import re

three_vowel = re.compile(r"(.*[aeiou]){3}")
letter_in_a_row = re.compile(r"(.)\1")
forbiden_string = re.compile(r"ab|cd|pq|xy")
letter_in_a_row_2 = re.compile(r"(..).*\1")
repeated_letter = re.compile(r"(.).\1")


def check_word(word, v2=False):
    if v2:
        if letter_in_a_row_2.search(word) and repeated_letter.search(word):
            return 1
    elif (
        three_vowel.search(word)
        and letter_in_a_row.search(word)
        and not forbiden_string.search(word)
    ):
        return 1
    return 0


def count_nice_words(words, v2=False):
    return sum(check_word(word, v2) for word in words)


if __name__ == "__main__":
    puzzle_input = Path("./src/aoc_2015/input/day_five.txt")
    words = puzzle_input.open().readlines()
    print(f"Nice words: {count_nice_words(words)}")
    print(f"Nice words: {count_nice_words(words, True)}")
