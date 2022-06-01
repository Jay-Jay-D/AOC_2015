from pathlib import Path
import re


def count_distinct_molecules(base_molecule, replacements):
    molecules = set()
    for replacement in replacements:
        base, replace = replacement.split(" => ")
        molecules.update(
            [
                f"{base_molecule[:m.start()]}{replace}{base_molecule[m.end():]}"
                for m in re.finditer(base, base_molecule)
            ]
        )
    return len(molecules)


def steps_needed(base_molecule, replacements):
    return None


if __name__ == "__main__":
    puzzle_input = Path("./src/aoc_2015/input/day_nineteen.txt")
    replacements = [l.strip() for l in puzzle_input.open().read().split("\n") if l]
    base_molecule = replacements.pop()
    molecules = count_distinct_molecules(base_molecule, replacements)
    print(f"Part 1: possible distinct molecules {molecules}")
    # Shamelees stolen
    steps = (
        len(re.findall(r"[A-Z]", base_molecule))
        - len(re.findall(r"(Rn)|(Ar)", base_molecule))
        - 2 * len(re.findall(r"Y", base_molecule))
        - 1
    )
    print(f"Part 2: possible distinct molecules {steps}")
