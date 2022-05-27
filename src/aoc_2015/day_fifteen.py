from dataclasses import asdict, dataclass
from joblib import Parallel, delayed


@dataclass
class Ingredient:
    name: str
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int


class Cookie:
    def __init__(self, ingredients_list):
        self.ingredient_list = ingredients_list
        self.properties = ["capacity", "durability", "flavor", "texture"]

    def get_score(self, *spoons, calories_limit=None):
        score = 1
        for property in self.properties:
            sum_by_property = 0
            calories_sum = 0
            for idx, ingredient in enumerate(self.ingredient_list):
                ingredient_spoons = spoons[idx]
                sum_by_property += asdict(ingredient)[property] * ingredient_spoons
                calories_sum += asdict(ingredient)["calories"] * ingredient_spoons
            if sum_by_property < 0 or (
                calories_limit is not None and calories_sum != calories_limit
            ):
                return 0
            score *= sum_by_property
        return score


# Shameless steal
def mixtures(n, total):
    start = total if n == 1 else 0

    for i in range(start, total + 1):
        left = total - i
        if n - 1:
            for y in mixtures(n - 1, left):
                yield [i] + y
        else:
            yield [i]


if __name__ == "__main__":
    # fmt:off
    ingredient_list = [
        Ingredient("Suggar",     3, 0,  0, -3, 2),
        Ingredient("Sprinkles", -3, 3,  0,  0, 9),
        Ingredient("Candy",     -1, 0,  4,  0, 1),
        Ingredient("Chocolate",  0, 0, -2,  2, 8),
    ]
    # fmt:on
    cookie = Cookie(ingredient_list)

    scores = Parallel(n_jobs=-1)(
        delayed(cookie.get_score)(*mixture) for mixture in mixtures(4, 100)
    )
    print(f"Part 1: Best score is {sorted(scores, reverse=True)[0]}")
    scores = Parallel(n_jobs=-1)(
        delayed(cookie.get_score)(*mixture, calories_limit=500) for mixture in mixtures(4, 100)
    )
    print(f"Part 2: Best score is {sorted(scores, reverse=True)[0]}")
