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

    # (path, visited_dac, visited_fft): num_paths
    positions = {("svr", False, False): 1}
    cntr = 0
    total = 0

    while len(positions.keys()) > 0:
        _positions = {}
        for position, num_paths in positions.items():
            path, visited_dac, visited_fft = position
            if path == "dac":
                visited_dac = True
            if path == "fft":
                visited_fft = True   
            outputs = devices[path]
            for output in outputs:
                key = (output, visited_dac, visited_fft)
                if output == "out":
                    total += num_paths
                    if visited_dac and visited_fft:
                        cntr += num_paths
                elif key not in _positions:
                    _positions[key] = num_paths
                else:
                    _positions[key] += num_paths

        positions = _positions

    print(f"{cntr=}, {total=}")


if __name__ == "__main__":
    solve_day_11()