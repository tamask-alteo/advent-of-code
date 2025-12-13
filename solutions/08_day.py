from dataclasses import dataclass, field
from itertools import combinations
from typing import Tuple, Dict, List
from math import prod


@dataclass(slots=True)
class Box:
    x: int
    y: int
    z: int
    id: int

    def __repr__(self) -> str:
        return f"[{self.x}, {self.y}, {self.z}]"
    
@dataclass(slots=True)
class Circuits:
    _circuits: Dict[int, List[int]] = field(default_factory=dict, repr=False)

    def get_num_circuits(self) -> int:
        return len(self._circuits.items())
    
    def merge_circuits(self, source: int, target: int) -> None:
        boxes_to_move = self._circuits[source]
        self._circuits[target].extend(boxes_to_move)
        _ = self._circuits.pop(source)

    def find_circuit(self, box: Box) -> int:
        for id, boxes in self._circuits.items():
            if box.id in boxes:
                return id

@dataclass(slots=True)
class Distances:
    _distances: Dict[Tuple[int, int], float] = field(default_factory=dict, repr=False)

    def add(self, box1: Box, box2: Box):
        distance = self._calculate_distance(box1, box2)
        key = self._make_key(box1, box2)
        self._distances[key] = distance

    def __getitem__(self, boxes: Tuple[Box, Box]) -> float:
        box1, box2 = boxes
        key = self._make_key(box1, box2)
        return self._distances[key]

    def get(self, box1: Box, box2: Box, default=None) -> float | None:
        key = self._make_key(box1, box2)
        return self._distances.get(key, default)

    def boxes_sorted(self):
        return sorted(self._distances.items(), key=lambda x: x[1])

    @staticmethod
    def _calculate_distance(box1: Box, box2: Box) -> float:
        return ((box1.x - box2.x) ** 2 + (box1.y - box2.y) ** 2 + (box1.z - box2.z) ** 2) ** 0.5

    @staticmethod
    def _make_key(box1: Box, box2: Box) -> Tuple[int, int]:
        return (box1.id, box2.id) if box1.id <= box2.id else (box2.id, box1.id)


def solve_day_8():
    with open("inputs/08_input.txt", "r") as f:
        boxes = [
            Box(*[int(x) for x in line.strip().split(",")], i) 
            for i, line in enumerate(f.readlines())
        ]

    circuits = Circuits({i: [b.id] for i, b in enumerate(boxes)})

    box_pairs = list(combinations(boxes, 2))
    distances = Distances()
    for b1, b2 in box_pairs:
        distances.add(b1, b2)

    counter = 0
    for (b1, b2), _ in distances.boxes_sorted():
        box1, box2 = boxes[b1], boxes[b2]
        circuit1, circuit2 = circuits.find_circuit(box1), circuits.find_circuit(box2)
        if circuit1 != circuit2:
            circuits.merge_circuits(source=circuit1, target=circuit2)

        counter += 1

        if counter == 1000: 
            num_boxes = [len(v) for k, v in circuits._circuits.items()]
            num_boxes.sort(reverse=True)
            print(f"{prod(num_boxes[:3])=}")

        if len(circuits._circuits.items()) == 1:
            print(f"{box1.x * box2.x=}")
            break


if __name__ == "__main__":
    solve_day_8()
