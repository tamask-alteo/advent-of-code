from dataclasses import dataclass, field
from typing import Tuple, List
from ast import literal_eval
from itertools import combinations_with_replacement
from copy import deepcopy


@dataclass(slots=True)
class Machine:
    light_diagram: Tuple[bool]
    buttons: Tuple[Tuple[int]]
    required_joltage_levels: Tuple[int]
    lights_on: List[bool] = field(init=False)
    joltage_levels: List[int] = field(init=False)
    num_buttons: int = field(init=False)

    def __post_init__(self):
        self.lights_on = [False] * len(self.light_diagram)
        self.joltage_levels = [0] * len(self.required_joltage_levels)
        self.num_buttons = len(self.buttons)

    def toggle_lights(self, button: int) -> None:
        lights_to_toggle = self.buttons[button]
        self.lights_on = [
            not light if i in lights_to_toggle else light for i, light in enumerate(self.lights_on)
        ]

    def increase_joltage(self, button: int) -> None:
        counters_to_increase = self.buttons[button]
        self.joltage_levels = [
            joltage + 1 if i in counters_to_increase else joltage for i, joltage in enumerate(self.joltage_levels)
        ]

    def check_if_lights_are_correct(self) -> bool:
        return list(self.light_diagram) == self.lights_on
    
    def check_if_joltages_are_correct(self) -> bool:
        return list(self.required_joltage_levels) == self.joltage_levels
    
    def copy(self) -> Machine:
        return deepcopy(self)

def parse_buttons(s: str) -> Tuple[int]:
    result = literal_eval(s)
    if not isinstance(result, tuple):
        return (result,)
    return result

def parse_joltages(s: str) -> Tuple[int]:
    result = literal_eval(s.replace("{", "(").replace("}", ")"))
    if not isinstance(result, tuple):
        return (result,)
    return result

def find_least_button_presses(machine: Machine, max_iterations: int = 100) -> int:
    for i in range(max_iterations):
        button_combinations = list(combinations_with_replacement(range(machine.num_buttons), i))
        for button_combination in button_combinations:
            _machine = machine.copy()
            for button in button_combination:
                _machine.toggle_lights(button)
                if _machine.check_if_lights_are_correct():
                    return i
                
def find_least_button_presses_2(machine: Machine, max_iterations: int = 100) -> int:
    for i in range(max_iterations):
        button_combinations = list(combinations_with_replacement(range(machine.num_buttons), i))
        for button_combination in button_combinations:
            _machine = machine.copy()
            for button in button_combination:
                _machine.increase_joltage(button)
                if _machine.check_if_joltages_are_correct():
                    return i


def solve_day_10():
    with open("inputs/10_input.txt", "r") as f:
        machines = []
        for line in f.readlines():
            tmp = line.strip().split(" ")
            light_diagram = tuple(True if light == "#" else False for light in tmp[0][1:-1])
            buttons = tuple(parse_buttons(b) for b in tmp[1:-1])
            required_joltage_levels = parse_joltages(tmp[-1])
            print(f"{required_joltage_levels=}")

            machine = Machine(light_diagram, buttons, required_joltage_levels)
            machines.append(machine)

    fewest_button_presses = [find_least_button_presses(machine, max_iterations=25) for machine in machines]
    print(f"{sum(fewest_button_presses)=}")

    fewest_button_presses_2 = [find_least_button_presses_2(machine, max_iterations=50) for machine in machines]
    print(f"{sum(fewest_button_presses_2)=}")

if __name__ == "__main__":
    solve_day_10()