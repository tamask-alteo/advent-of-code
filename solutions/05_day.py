from typing import List
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Range:
    start: int
    end: int

    @property
    def length(self) -> int:
        return self.end - self.start + 1
    
    def __repr__(self) -> str:
        return f"[{self.start}, {self.end}]"
    
    def check_overlap(self, other: Range) -> bool:
        return (
            other.start <= self.start <= other.end
            or other.start <= self.end <= other.end
        )
    
    def merge(self, other: Range) -> Range:
        return Range(
            min(self.start, other.start),
            max(self.end, other.end)
        )

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

    fresh_ingredients = []
    for i in ingedients:
        if check_if_ingredient_is_fresh(ranges, i):
            fresh_ingredients.append(i)

    print(f"{len(fresh_ingredients)=}")

    found_overlap = True
    while found_overlap:
        found_overlap = False

        ranges = sorted(ranges, key=lambda x: (x.start, x.end))

        disjunct_ranges = ranges[:1]
        for r in ranges[1:]:
            _last_range = disjunct_ranges[-1]
            if r.check_overlap(_last_range):
                disjunct_ranges[-1] = _last_range.merge(r)
                found_overlap = True
            else:
                disjunct_ranges += [r]
        
        ranges = disjunct_ranges.copy()

    print(f"{sum([r.length for r in disjunct_ranges])=}")


if __name__ == "__main__":
    solve_day_5()
