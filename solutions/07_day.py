from dataclasses import dataclass
from typing import List, Tuple
from collections import Counter


@dataclass(frozen=True, slots=True)
class Beams:
    data: List[Beam]

    def __repr__(self):
        return str(self.data)
    
    def split_beams(self, splits: Splits) -> Tuple[Beams, int]:
        new_beams = []
        split_cnt = 0
        for beam in self.data:
            if beam.position in splits.list_splits():
                new_beams += [
                    Beam(beam.position - 1, beam.path_count),
                    Beam(beam.position + 1, beam.path_count)
                ]
                split_cnt += 1
            else:
                new_beams += [beam]

        totals = Counter()
        for beam in new_beams:
            totals[beam.position] += beam.path_count
        unique_beams = [Beam(pos, count) for pos, count in totals.items()]

        return (Beams(unique_beams), split_cnt)

@dataclass(frozen=True, slots=True)
class Beam:
    position: int
    path_count: int = 1

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

    starting_beam = Beam(lines[0].find("S"), path_count=1)

    beams = Beams([starting_beam])
    manifold = [[i for i, ch in enumerate(line) if ch == "^"] for line in lines[1:-1]]
    manifold = [Splits(x) for x in manifold if len(x) > 0]

    total_split_count = 0
    for splits in manifold:
        beams, split_cnt = beams.split_beams(splits)
        total_split_count += split_cnt

    print(f"{total_split_count=}")
    print(f"{sum([b.path_count for b in beams.data])=}")


if __name__ == "__main__":
    solve_day_7()
