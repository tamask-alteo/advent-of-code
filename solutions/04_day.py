from dataclasses import dataclass
from typing import List


@dataclass(frozen=True, slots=True)
class Grid:
    data: List[List[bool]]

    def __repr__(self) -> str:
        return "\n".join(["".join(["@" if v else "." for v in row]) for row in self.data])

    @property
    def nrows(self) -> int:
        return len(self.data)

    @property
    def ncols(self) -> int:
        return len(self.data[0]) if self.data else 0

    def __getitem__(self, rc: tuple[int, int], default: bool = False) -> bool:
        r, c = rc
        if not (0 <= r < self.nrows and 0 <= c < self.ncols):
            return default
            
        return self.data[r][c]
    
    def get_all_coordinates(self) -> List[List[int]]:
        return [[r, c] for c in range(self.ncols) for r in range(self.nrows)]
    
    def remove_roll(self, rc: tuple[int, int]) -> None:
        r, c = rc
        self.data[r][c] = False


def solve_day_4():
    with open("inputs/04_input.txt", "r") as f:
        grid = Grid([[x == "@" for x in line.strip()] for line in f.readlines()])
    
    neighbours = [[i, j] for j in [-1, 0, 1] for i in [-1, 0, 1] if not (i == 0 and j == 0)]
    grid_coordinates = grid.get_all_coordinates()

    cnt = 0
    for r, c in grid_coordinates:
        if not grid[r, c]: # not a roll
            continue

        cnt_adjacent_trues = 0
        for i, j in neighbours:
                _r = r + i
                _c = c + j
                
                cnt_adjacent_trues += 1 if grid[_r, _c] else 0

        if cnt_adjacent_trues < 4:
            cnt += 1

    print(f"{cnt=}")

    cnt_2 = 0
    made_removal = True

    while made_removal:
        made_removal = False
        
        for r, c in grid_coordinates:
            if not grid[r, c]: # not a roll
                continue

            cnt_adjacent_trues = 0
            for i, j in neighbours:
                    _r = r + i
                    _c = c + j
                    
                    cnt_adjacent_trues += 1 if grid[_r, _c] else 0

            if cnt_adjacent_trues < 4:
                cnt_2 += 1
                grid.remove_roll((r, c))
                made_removal = True
                break

    print(f"{cnt_2=}")


if __name__ == "__main__":
    solve_day_4()
