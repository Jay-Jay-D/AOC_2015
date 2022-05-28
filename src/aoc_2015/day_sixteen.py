from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass
class aunts:
    Sue: int
    children: int = None
    cats: int = None
    samoyeds: int = None
    pomeranians: int = None
    akitas: int = None
    vizslas: int = None
    goldfish: int = None
    trees: int = None
    cars: int = None
    perfumes: int = None

    @classmethod
    def parse(cls, aunt_sue_data):
        parts = aunt_sue_data.strip().replace(",", "").replace(":", "").split(" ")
        return cls(**{parts[idx]: int(parts[idx + 1]) for idx in range(0, len(parts) - 1, 2)})

    @staticmethod
    def parse_aunts(aunts_sue_data):
        return [aunts.parse(aunt_sue) for aunt_sue in aunts_sue_data]

    def matches(self, target, retroencabulator=False) -> bool:
        target = asdict(target)
        for key, value in asdict(self).items():
            if key == "Sue" or value is None:
                continue
            if retroencabulator and key in ["cats", "trees", "pomeranians", "goldfish"]:
                if (key in ["cats", "trees"] and value > target[key]) or (
                    key in ["pomeranians", "goldfish"] and value < target[key]
                ):
                    continue
                else:
                    return False
            if value == target[key]:
                continue
            else:
                return False
        return True


if __name__ == "__main__":
    input_file = Path("./src/aoc_2015/input/day_sixteen.txt")
    aunt_sues_data = input_file.open().readlines()

    aunt_looking_for = {
        "Sue": -1,
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1,
    }

    aunts_sues = aunts.parse_aunts(aunt_sues_data)
    aunt_looking_for = aunts(**aunt_looking_for)

    for aunt in aunts_sues:
        if aunt.matches(aunt_looking_for):
            print(f"Part 1: the aunt Sue number {aunt.Sue} matches!")
        if aunt.matches(aunt_looking_for, True):
            print(f"Part 2: the aunt Sue number {aunt.Sue} matches!")
