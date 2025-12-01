START = 50
MAX = 99

def rotate(start: int, instruction: str) -> int:
    direction = instruction[0]
    clicks = int(instruction[1:])
    if direction == "L":
        position = start - clicks
        if position < 0:
            position = MAX + 1 + position
    else:
        position = start + clicks
        
    return position % (MAX + 1)

def solve_day_1():
    print(f"{START=}")
    print(f"{MAX=}")

    with open("inputs/01_input.txt", "r") as f:
        input = [line.strip() for line in f.readlines()]

    print(f"{input=}")

    zero_counter = 0
    direction = START
    for i in input:
        direction = rotate(direction, i)
        print(f"{i=}, {direction=}")

        if direction == 0:
            zero_counter += 1

    print(f"{zero_counter=}")
    


if __name__ == "__main__":
    solve_day_1()
