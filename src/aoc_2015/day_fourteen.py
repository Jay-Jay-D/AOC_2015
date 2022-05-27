from dataclasses import dataclass
from math import inf
from pathlib import Path


class Race:
    def __init__(self, reindeer_specs):
        self.reindeers = [
            Reindeer.generate_from_specs(reindeer_spec) for reindeer_spec in reindeer_specs
        ]
        self.wining_reindeer = None

    def advance_second(self):
        max_distance = -inf
        for reindeer in self.reindeers:
            reindeer.advance_second()
            if reindeer.distance >= max_distance:
                max_distance = reindeer.distance
        for reindeer in self.reindeers:
            if reindeer.distance == max_distance:
                reindeer.points += 1
        self.wining_reindeer = sorted(self.reindeers, key=lambda r: r.points, reverse=True)[0]

    def run(self, seconds):
        [self.advance_second() for _ in range(seconds)]


@dataclass
class Reindeer:
    name: str
    speed: int
    run_lenght: int
    rest: int

    def __init__(self, name, speed, run_lenght, rest):
        self.name = name
        self.speed = speed
        self.run_lenght = run_lenght
        self.rest = rest
        self.time = 0
        self.distance = 0
        self.points = 0
        self.lap_time = 0

    @classmethod
    def generate_from_specs(cls, reindeer_spec):
        parts = reindeer_spec.strip().split(" ")
        name = parts[0]
        speed = int(parts[3])
        run_lenght = int(parts[6])
        rest = int(parts[-2])
        return cls(name, speed, run_lenght, rest)

    def advance_second(self):
        self.lap_time += 1
        self.time += 1
        if self.lap_time <= self.run_lenght:
            self.distance += self.speed
        if self.lap_time == self.run_lenght + self.rest:
            self.lap_time = 0


if __name__ == "__main__":
    input_file = Path("./src/aoc_2015/input/day_fourteen.txt")
    reindeer_specs = input_file.open().readlines()
    race = Race(reindeer_specs)
    race.run(2503)
    print(f"Part 2: The winning reindeer has {race.wining_reindeer.points} points.")
