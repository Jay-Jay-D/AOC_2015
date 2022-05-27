import pytest

from aoc_2015.day_fourteen import Race, Reindeer


reindeers_specs = [
    "Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.",
    "Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.",
]


def test_reindeer_advance_second():
    # Arrange
    reindeer = Reindeer(name="Dancer", speed=14, run_lenght=10, rest=127)
    # Act
    reindeer.advance_second()
    # Arrange
    assert reindeer.distance == 14
    assert reindeer.time == 1


def test_reindeer_resting():
    # Arrange
    reindeer = Reindeer(name="Dancer", speed=14, run_lenght=10, rest=50)
    # Act
    [reindeer.advance_second() for _ in range(11)]
    # Arrange
    assert reindeer.distance == 140
    assert reindeer.time == 11
    # Act
    [reindeer.advance_second() for _ in range(49)]
    # Arrange
    assert reindeer.distance == 140
    assert reindeer.time == 60
    # Act
    reindeer.advance_second()
    # Arrange
    assert reindeer.distance == 154
    assert reindeer.time == 61


def test_generate_race():
    # Arrange
    expected_reindeers = [
        Reindeer(name="Comet", speed=14, run_lenght=10, rest=127),
        Reindeer(name="Dancer", speed=16, run_lenght=11, rest=162),
    ]
    # Act
    race = Race(reindeers_specs)
    # Assert
    assert len(expected_reindeers) == len(race.reindeers)
    assert all(expected == actual for expected, actual in zip(expected_reindeers, race.reindeers))


def test_race_steps():
    # Arrange
    race = Race(reindeers_specs)
    comet = race.reindeers[0]
    dancer = race.reindeers[1]
    # Act
    race.advance_second()
    # Assert
    assert comet.distance == 14
    assert dancer.distance == 16
    assert comet.points == 0
    assert dancer.points == 1
    # Act
    race.run(139)
    # Assert
    assert comet.distance == 182
    assert dancer.distance == 176
    assert comet.points == 1
    assert dancer.points == 139


def test_race():
    # Arrange
    race = Race(reindeers_specs)
    # Act
    race.run(1000)
    # Assert
    assert race.wining_reindeer.points == 689
