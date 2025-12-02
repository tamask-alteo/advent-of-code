def check_if_invalid_part1(x: int) -> bool:
    s = str(x)
    num_char = len(s)
    if num_char % 2 != 0:
        return False
    
    middle = int(num_char / 2)
    if s[:middle] == s[middle:]:
        return True
    
    return False

def check_if_invalid_part2(x: int) -> bool:
    s = str(x)
    num_char = len(s)
    
    for i in range(1, int(num_char / 2) + 1):
        if num_char % i == 0:
            reps = int(num_char / i)
            if s[:i] * reps == s:
                return True
    
    return False


def solve_day_2():
    with open("inputs/02_input.txt", "r") as f:
        ranges = [
            [int(x) for x in r.split("-")] for r in f.readlines()[0].split(",")
        ]

    invalid_ids_part1 = []
    invalid_ids_part2 = []
    for r in ranges:
        for x in range(r[0], r[1] + 1):
            if check_if_invalid_part1(x):
                invalid_ids_part1.append(x)

            if check_if_invalid_part2(x):
                invalid_ids_part2.append(x)

    print(f"{sum(invalid_ids_part1)=}")
    print(f"{sum(invalid_ids_part2)=}")


if __name__ == "__main__":
    solve_day_2()
