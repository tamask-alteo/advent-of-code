def solve_day_11():
    devices = {}
    with open("inputs/11_input.txt", "r") as f:
        for line in f.readlines():
            tmp = line.strip().split(": ")
            devices[tmp[0]] = tmp[1].split(" ")

    positions = {"you": 1}
    cntr = 0

    while len(positions.keys()) > 0:
        _positions = {}
        for position, num_paths in positions.items():
                outputs = devices[position]
                for output in outputs:
                    if output == "out":
                        cntr += num_paths
                    elif output not in _positions:
                        _positions[output] = num_paths
                    else:
                        _positions[output] += num_paths

        positions = _positions

    print(f"{cntr=}")

    
if __name__ == "__main__":
    solve_day_11()