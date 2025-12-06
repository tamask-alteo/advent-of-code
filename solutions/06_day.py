from typing import List, Literal
from dataclasses import dataclass
from math import prod


@dataclass(frozen=True, slots=True)
class Operation:
    operation: Literal["+", "*"]

    def __repr__(self):
        return self.operation

    def apply(self, x: List[int]):
        if self.operation == "+":
            return sum(x)
        else:
            return prod(x)

@dataclass(frozen=True, slots=True)
class Block:
    start: int
    end: int

def solve_day_6():
    with open("inputs/06_input.txt", "r") as f:
        input = [line.strip().split() for line in f.readlines()]

    print(f"{input=}")

    operations = [Operation(o) for o in input[-1]]
    
    num_numbers_per_problem = len(input[0])
    numbers = [[int(row[c]) for row in input[:-1]] for c in range(num_numbers_per_problem)]

    print(f"{sum(operation.apply(numbers[i]) for i, operation in enumerate(operations))}")

    # PART 2----
    with open("inputs/06_input.txt", "r") as f:
        input = [line.replace("\n", "") for line in f.readlines()]

        positions = [i for i, ch in enumerate(input[-1]) if ch in "*+"] + [max([len(x) for x in input[:-1]])]
        blocks = [Block(*x) for x in zip(positions, positions[1:])]

        foo = []
        for block in blocks:
            bar = []
            for row in input[:-1]:
                bar.append(row[block.start:(block.end)])
            
            baz = []
            for i, _ in enumerate(bar[0]):
                meow = ''
                for j, _ in enumerate(bar):
                    meow += bar[j][i]

                if not meow.strip() == '':
                    baz.append(meow)

            foo.append(baz)

        print(f"{sum(operation.apply([int(x) for x in foo[i]]) for i, operation in enumerate(operations))}")


if __name__ == "__main__":
    solve_day_6()
