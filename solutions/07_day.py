from dataclasses import dataclass
from typing import List, Tuple


@dataclass(frozen=True, slots=True)
class Beams:
    data: List[int]

    def __repr__(self):
        return str(self.data)
    
    def split_beams(self, splits: Splits) -> Tuple[Beams, int]:
        new_beams = []
        split_cnt = 0
        for beam in self.data:
            if beam in splits.list_splits():
                new_beams += [beam - 1, beam + 1]
                split_cnt += 1
            else:
                new_beams += [beam]

        new_beams = list(set(new_beams))
        new_beams.sort()

        return (Beams(new_beams), split_cnt)


@dataclass(frozen=True, slots=True)
class Splits:
    data: List[int]

    def __repr__(self):
        return str(self.data)
    
    def list_splits(self) -> List[int]:
        return self.data


def solve_day_7():
    with open("inputs/07_input.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    start = lines[0].find("S")

    beams = Beams([start])
    manifold = [[i for i, ch in enumerate(line) if ch == "^"] for line in lines[1:-1]]
    manifold = [Splits(x) for x in manifold if len(x) > 0]

    total_split_count = 0
    for splits in manifold:
        beams, split_cnt = beams.split_beams(splits)
        total_split_count += split_cnt

    print(f"{total_split_count=}")


if __name__ == "__main__":
    solve_day_7()
