from typing import List
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Range:
    start: int
    end: int
    
    def __repr__(self) -> str:
        return f"[{self.start}, {self.end}]"
    

def check_if_ingredient_is_fresh(ranges: List[Range], ingredient: int) -> bool:
    for r in ranges:
        if r.start <= ingredient <= r.end:
            return True
        
    return False


def solve_day_5():
    with open("inputs/05_input.txt", "r") as f:
        ranges = []
        ingedients = []
        processing_ingredients = False
        for line in f.readlines():
            _line = line.strip()
            if not processing_ingredients:
                if _line == "":
                    processing_ingredients = True
                else:
                    ranges.append(Range(*[int(x) for x in _line.split("-")]))
            else:
                ingedients.append(int(_line))
        
    print(f"{ranges=}")
    print(f"{ingedients=}")

    fresh_ingredients = []
    for i in ingedients:
        if check_if_ingredient_is_fresh(ranges, i):
            fresh_ingredients.append(i)

    print(f"{fresh_ingredients=}")
    print(f"{len(fresh_ingredients)=}")


if __name__ == "__main__":
    solve_day_5()