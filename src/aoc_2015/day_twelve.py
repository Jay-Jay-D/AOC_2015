import json
from pathlib import Path


class JsonExplorer:
    def __init__(self, path_to_json_file, ignore_red=False):
        json_file = Path(path_to_json_file)
        json_obj = json.load(json_file.open())
        self.integer_sum = 0
        self.ignore_red = ignore_red
        self.explore_object(json_obj)

    def explore_object(self, obj):
        if isinstance(obj, dict):
            if self.ignore_red and "red" in obj.values():
                return
            for value in obj.values():
                self.explore_object(value)
        if isinstance(obj, list):
            for value in obj:
                self.explore_object(value)
        if isinstance(obj, int):
            self.integer_sum += obj


if __name__ == "__main__":
    explorer = JsonExplorer("./src/aoc_2015/input/day_twelve.json")
    print(f"Part 1 - JSON integer sum: {explorer.integer_sum}")
    explorer = JsonExplorer("./src/aoc_2015/input/day_twelve.json", True)
    print(f"Part 2 - JSON integer sum: {explorer.integer_sum}")
