START = 50
CAP = 100

def parse_clicks(instruction: str) -> int:
    direction = instruction[0]
    clicks = int(instruction[1:])
    if direction == "L":
        clicks = -1 * clicks

    return clicks

def parse_rotations_and_remaining_clicks(clicks: int) -> tuple[int, int]:
    if clicks == 0:
        return (0, 0)
    
    if clicks > 0:
        rotations = clicks // CAP
        clicks = clicks % CAP
    else:
        clicks = abs(clicks)
        rotations = clicks // CAP
        clicks = -1 * (clicks % CAP)

    return (rotations, clicks)

def solve_day_1():
    with open("inputs/01_input.txt", "r") as f:
        instructions = [parse_clicks(line.strip()) for line in f.readlines()]

    print(f"{instructions=}")

    zero_counter = 0
    zero_counter_2 = 0
    position = START
    for clicks in instructions:
        rotations, clicks = parse_rotations_and_remaining_clicks(clicks)
        
        previous_position = position

        position = position + clicks

        if position < 0 and previous_position != 0:
            rotations += 1
        if position > 100:
            rotations += 1

        position = position % CAP
        
        if position == 0:
            zero_counter += 1
            rotations += 1

        zero_counter_2 += rotations

    print(f"{zero_counter=}")
    print(f"{zero_counter_2=}")
    

if __name__ == "__main__":
    solve_day_1()
