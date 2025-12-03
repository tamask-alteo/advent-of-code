def solve_day_3():
    with open("inputs/03_input.txt", "r") as f:
        banks = [[int(x) for x in line.strip()] for line in f.readlines()]

    print(f"{banks=}")

    largest_joltages = []
    for bank in banks:
        first_digit_index, first_digit = max(enumerate(bank[:-1]), key=lambda x: x[1])
        _, second_digit = max(enumerate(bank[(first_digit_index + 1):]), key=lambda x: x[1])

        largest_joltages.append(first_digit * 10 + second_digit)

    print(f"{sum(largest_joltages)=}")

if __name__ == "__main__":
    solve_day_3()