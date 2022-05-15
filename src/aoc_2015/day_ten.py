def say(sequence):
    reading = ""
    element = sequence[0]
    element_count = 1
    for idx in range(1, len(sequence)):
        if sequence[idx] == element:
            element_count += 1
        else:
            reading += f"{element_count}{element}"
            element = sequence[idx]
            element_count = 1
    reading += f"{element_count}{element}"
    return reading


def say_many_times(sequence, times):
    for _ in range(times):
        sequence = say(sequence)
    return sequence


if __name__ == "__main__":
    print(f"Part one - length of the result: {len(say_many_times('1321131112', 40))}")
    print(f"Part two - length of the result: {len(say_many_times('1321131112', 50))}")
