from sympy import divisors
from joblib import Parallel, delayed


def get_gifts_to_house(house, part_two=False):
    if isinstance(house, list):
        return [get_gifts_to_house(h, part_two) for h in house]
    if part_two:
        return house, sum(elf * 11 if house / elf <= 50 else 0 for elf in divisors(house))
    else:
        return house, sum(elf * 10 for elf in divisors(house))


def get_house_with_gifts(gifts_target, part_two=False):
    gifts = 0
    subset_size = 1000
    bacth_start = step = 1
    while gifts < gifts_target:
        batch_results = Parallel(n_jobs=-1)(
            delayed(get_gifts_to_house)(list(range(i, i + subset_size)), part_two)
            for i in range(bacth_start, step * subset_size * 10, subset_size)
        )
        bacth_start = step * subset_size * 10 + 1
        step += 1
        for b in batch_results:
            for r in b:
                if r[1] > gifts:
                    gifts = r[1]
                    house = r[0]
    return house


if __name__ == "__main__":
    gifts_target = 34000000
    house = get_house_with_gifts(gifts_target)
    print(f"Part 1: first house with at least {gifts_target} is house {house}.")
    house = get_house_with_gifts(gifts_target, True)
    print(f"Part 2: first house with at least {gifts_target} is house {house}.")
