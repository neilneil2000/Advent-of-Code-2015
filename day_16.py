from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class AuntSue:
    """Dataclass representing what I know about Aunt Sue"""

    number: int = None
    stuff: Dict[str, int] = field(default_factory=dict)


def get_sues(filename: str) -> List[AuntSue]:
    """Read information about sues from file with filename"""
    sues = []
    with open(filename, mode="r", encoding="utf-8") as f:
        sue_descriptions = f.readlines()
    for sue_desc in sue_descriptions:
        sue = sue_desc.split()
        new_sue = AuntSue(number=int(sue[1][:-1]))
        for parameter in sue[2:]:
            if parameter[-1] == ":":  # descriptor
                descriptor = parameter[:-1]
            else:  # value
                try:
                    new_sue.stuff[descriptor] = int(parameter)
                except ValueError:
                    new_sue.stuff[descriptor] = int(parameter[:-1])
        sues.append(new_sue)

    return sues


def main():
    """Main Solution"""
    gifting_sue = AuntSue(
        number=0,
        stuff={
            "children": 3,
            "cats": 7,
            "samoyeds": 2,
            "pomeranians": 3,
            "akitas": 0,
            "vizslas": 0,
            "goldfish": 5,
            "trees": 3,
            "cars": 2,
            "perfumes": 1,
        },
    )
    sues = get_sues("day_16_input.txt")

    correct_sue = None
    for sue in sues:
        if all(item in gifting_sue.stuff.items() for item in sue.stuff.items()):
            correct_sue = sue
            break
    print(correct_sue.number)


if __name__ == "__main__":
    main()
