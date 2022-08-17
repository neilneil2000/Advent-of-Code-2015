"""Advent of Code 2015 Day 7"""

from day_7_circuit import Circuit
from day_7_input import puzzle_input


def main():
    """Main Function"""

    my_circuit = Circuit()
    for instruction in puzzle_input.splitlines():
        my_circuit.add_gate(instruction)

    wire_name = "a"
    wire_signal = my_circuit.get_wire_value(wire_name)
    print(f"Wire {wire_name} has a value of: {wire_signal}")

    my_second_circuit = Circuit()
    for instruction in puzzle_input.splitlines():
        if instruction[-4:] == "-> b":
            instruction = f"{wire_signal} -> b"
        my_second_circuit.add_gate(instruction)

    wire_signal = my_second_circuit.get_wire_value(wire_name)
    print(f"Wire {wire_name} has a value of: {wire_signal}")


if __name__ == "__main__":
    main()
