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

def solve_day_6():
    with open("inputs/06_input.txt", "r") as f:
        input = [line.strip().split() for line in f.readlines()]

        operations = [Operation(o) for o in input[-1]]
        
        num_numbers_per_problem = len(input[0])
        numbers = [[int(row[c]) for row in input[:-1]] for c in range(num_numbers_per_problem)]

    # print(f"{operations=}")
    # print(f"{numbers=}")
    print(f"{sum(operation.apply(numbers[i]) for i, operation in enumerate(operations))}")


if __name__ == "__main__":
    solve_day_6()
