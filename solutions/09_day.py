from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Tile:
    x: int
    y: int

    def __repr__(self) -> str:
        return f"[{self.x}, {self.y}]"

def calculate_rectange_size(tile_1: Tile, tile_2: Tile) -> int:
    min_x = min(tile_1.x, tile_2.x)
    max_x = max(tile_1.x, tile_2.x)
    
    min_y = min(tile_1.y, tile_2.y)
    max_y = max(tile_1.y, tile_2.y)

    return (max_x - min_x + 1) * (max_y - min_y + 1)


def solve_day_9():
    with open("inputs/09_input.txt", "r") as f:
        red_tiles = [
            Tile(*[int(x) for x in line.strip().split(",")]) for line in f.readlines()
        ]

    pairs = [[tile_1, tile_2] for tile_1 in red_tiles for tile_2 in red_tiles if tile_1 != tile_2]
    max_size = max([calculate_rectange_size(tile_1, tile_2) for tile_1, tile_2 in pairs])

    print(f"{max_size=}")

if __name__ == "__main__":
    solve_day_9()
