from typing import List


def find_largest_joltage(bank: List[int], num_batteries: int = 2) -> int:
    digits = []
    digit_index = -1
    _bank = bank.copy()
    for i in range(num_batteries):
        _bank = _bank[(digit_index + 1):]
        digit_index, digit = max(
            enumerate(_bank[:len(_bank)-num_batteries+i+1]), 
            key=lambda x: x[1]
        )

        digits.append(digit)
    
    return sum([d * (10 ** (num_batteries - i - 1)) for i, d in enumerate(digits)])

def solve_day_3():
    with open("inputs/03_input.txt", "r") as f:
        banks = [[int(x) for x in line.strip()] for line in f.readlines()]

    largest_joltages_part_1 = [find_largest_joltage(bank, 2) for bank in banks]
    largest_joltages_part_2 = [find_largest_joltage(bank, 12) for bank in banks]

    print(f"{sum(largest_joltages_part_1)=}")
    print(f"{sum(largest_joltages_part_2)=}")


if __name__ == "__main__":
    solve_day_3()