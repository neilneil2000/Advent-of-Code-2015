"""Circuit Emulation Module for Day 7"""

from day_7_gates import (
    OneInputLogicGate,
    TwoInputLogicGate,
    GateDescription,
    logic_gate_factory,
)


class Circuit:
    """Representation of a Circuit"""

    def __init__(self):
        self.wires = {}  # wire_name:signal_value
        self.gates = []

    def add_gate(self, instruction: str):
        """Add gate to circuit"""
        new_gate_description = self._parse_instruction(instruction)
        new_gate = logic_gate_factory(new_gate_description)
        if new_gate_description.input_a.isdigit():
            if isinstance(new_gate, OneInputLogicGate):
                new_gate.input.signal = int(new_gate_description.input_a)
            else:
                new_gate.input_a.signal = int(new_gate_description.input_a)

        if (
            new_gate_description.input_b
            and new_gate_description.input_b.isdigit()
            and isinstance(new_gate, TwoInputLogicGate)
        ):
            new_gate.input_b.signal = int(new_gate_description.input_b)

        self.gates.append(new_gate)

    def get_wire_value(self, wire_name: str) -> int:
        """Recursive function that returns signal value for given wire"""
        if wire_name not in self.wires:
            for gate in self.gates:
                if gate.output.name != wire_name:
                    continue  # This is not the gate you're looking for!
                if not gate.inputs_valid():
                    newly_calculated_wires = {}
                    for input_name in gate.invalid_input_names:
                        newly_calculated_wires[input_name] = self.get_wire_value(
                            input_name
                        )
                    gate.set_inputs(newly_calculated_wires)

                gate.compute_output()
                self.wires[gate.output.name] = gate.output.signal
                break

        return self.wires[wire_name]

    @staticmethod
    def _parse_instruction(instruction: str) -> GateDescription:
        """Parse Instruction
        Return Format: (input_a, input_b, operation, output)
        """
        # 123 -> x
        # lx -> a
        # x AND y -> d
        # x OR y -> e
        # x LSHIFT 2 -> f
        # y RSHIFT 2 -> g
        # NOT x -> h
        left, right = instruction.split("->")
        left = left.split()
        right = right.strip()
        if len(left) == 1:
            return GateDescription(left[0], None, None, right)
        if len(left) == 2:
            return GateDescription(left[1], None, left[0], right)
        return GateDescription(left[0], left[2], left[1], right)
