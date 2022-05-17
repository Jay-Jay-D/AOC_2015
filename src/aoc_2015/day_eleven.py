import re


def get_three_consecutives_letters_set():
    output = []
    for i in range(99, 123):
        three_letter_seq = bytearray([i - 2, i - 1, i]).decode()
        if ("i" in three_letter_seq) or ("o" in three_letter_seq) or ("l" in three_letter_seq):
            continue
        output.append(three_letter_seq)
    return output


def incremment_string(input):
    output = []
    carry = True
    for c in reversed(input):
        c, carry = increment_char(c, carry)
        output.append(c)
    return "".join(reversed(output))


def increment_char(input, carry=True):
    if not carry:
        return input, carry

    char_as_ord = ord(str.encode(input)) + 1
    if char_as_ord in [105, 108, 111]:
        char_as_ord += 1
    if char_as_ord < 123:
        carry = False
    else:
        char_as_ord = 97
    return bytearray([char_as_ord]).decode(), carry


def get_next_password(password):
    three_letter_seq = get_three_consecutives_letters_set()
    while True:
        password = incremment_string(password)
        if ("i" in password) or ("o" in password) or ("l" in password):
            continue
        if len(re.findall(r"([a-z])\1", password)) < 2:
            continue
        if any(seq in password for seq in three_letter_seq):
            break
    return password


if __name__ == "__main__":
    origial_password = "cqjxjnds"
    next_pasword = get_next_password(origial_password)
    print(f"Part One - Next password after {origial_password} is {next_pasword}")
    after_next_pasword = get_next_password(next_pasword)
    print(f"Part Two - Next password after {next_pasword} is {after_next_pasword}")
