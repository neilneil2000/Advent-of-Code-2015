"""Logic Gate Module for Day 7"""

from abc import ABC, abstractmethod, abstractproperty
from collections import namedtuple
from dataclasses import dataclass
from enum import Enum, auto
from typing import Dict, List


GateDescription = namedtuple(
    "GateDescription", ["input_a", "input_b", "operation", "output"]
)


class GateType(Enum):
    """Enumeration of Gate Types"""

    DIRECT = auto()
    AND = auto()
    NOT = auto()
    OR = auto()
    LSHIFT = auto()
    RSHIFT = auto()


@dataclass
class Wire:
    """Data Class Representing a Wire"""

    name: str = ""
    signal: int = None


class LogicGate(ABC):
    """Representation of a Logic Gate"""

    def __init__(self, gate_type: GateType, output_name: str):
        self.type = gate_type
        self.output = Wire(name=output_name)

    @abstractproperty
    def invalid_input_names(self) -> List[str]:
        """Returns List of all inputs with a signal value of None"""

    @abstractmethod
    def inputs_valid(self) -> bool:
        """Returns True if all inputs are valid"""

    @abstractmethod
    def compute_output(self) -> bool:
        """Calculate Value on output wire, from input wires"""

    @abstractmethod
    def set_inputs(self, inputs: Dict[str, int]) -> None:
        """Set Inputs to values in inputs list"""


class OneInputLogicGate(LogicGate):
    """One Input Logic Gate (ABSTRACT)"""

    def __init__(self, gate_type: GateType, input_name, output_name):
        super().__init__(gate_type, output_name)
        self.input = Wire(name=input_name)
        if self.input.name.isdigit():
            self.input.signal = int(self.input.name)

    def inputs_valid(self) -> bool:
        return self.input.signal is not None

    def set_inputs(self, inputs: Dict[str, int]) -> None:
        for input_name, input_signal in inputs.items():
            if input_name == self.input.name:
                self.input.signal = input_signal

    @property
    def invalid_input_names(self) -> List[str]:
        if self.input.signal is None:
            return [self.input.name]
        return []


class TwoInputLogicGate(LogicGate):
    """Two input Logic Gate (ABSTRACT)"""

    def __init__(self, gate_type: GateType, input_a_name, input_b_name, output_name):
        super().__init__(gate_type, output_name)
        self.input_a = Wire(name=input_a_name)
        if self.input_a.name.isdigit():
            self.input_a.signal = int(self.input_a.name)
        self.input_b = Wire(name=input_b_name)
        if self.input_b.name.isdigit():
            self.input_b.signal = int(self.input_b.name)

    def inputs_valid(self) -> bool:
        return self.input_a.signal is not None and self.input_b.signal is not None

    def set_inputs(self, inputs: Dict[str, int]) -> None:
        for input_name, input_signal in inputs.items():
            if input_name == self.input_a.name:
                self.input_a.signal = input_signal
            elif input_name == self.input_b.name:
                self.input_b.signal = input_signal

    @property
    def invalid_input_names(self) -> List[str]:
        invalid_signals = []
        for wire in [self.input_a, self.input_b]:
            if wire.signal is None:
                invalid_signals.append(wire.name)
        return invalid_signals


class ShiftLogicGate(LogicGate):
    """Bitwise Shifting Logic Gate (ABSTRACT)"""

    def __init__(self, gate_type: GateType, input_name, shift_places, output_name):
        super().__init__(gate_type, output_name)
        self.input = Wire(name=input_name)
        if self.input.name.isdigit():
            self.input.signal = int(self.input.name)
        self.shift_places = int(shift_places)

    def inputs_valid(self) -> bool:
        return self.input.signal is not None

    def set_inputs(self, inputs: Dict[str, int]) -> None:
        for input_name, input_signal in inputs.items():
            if input_name == self.input.name:
                self.input.signal = input_signal

    @property
    def invalid_input_names(self) -> List[str]:
        if self.input.signal is None:
            return [self.input.name]
        return []


class DirectGate(OneInputLogicGate):
    """Direct Connection"""

    def __init__(self, input_name, output_name):
        super().__init__(GateType.DIRECT, input_name, output_name)

    def compute_output(self) -> bool:
        if not self.inputs_valid():
            return False
        self.output.signal = self.input.signal
        return True

    @property
    def invalid_input_names(self) -> List[str]:
        return super().invalid_input_names


class AndGate(TwoInputLogicGate):
    """Two Input AND Gate"""

    def __init__(self, input_a_name, input_b_name, output_name):
        super().__init__(GateType.AND, input_a_name, input_b_name, output_name)

    def compute_output(self) -> bool:
        if not self.inputs_valid():
            return False
        self.output.signal = self.input_a.signal & self.input_b.signal
        return True

    @property
    def invalid_input_names(self) -> List[str]:
        return super().invalid_input_names


class OrGate(TwoInputLogicGate):
    """Two Input OR Gate"""

    def __init__(self, input_a_name, input_b_name, output_name):
        super().__init__(GateType.OR, input_a_name, input_b_name, output_name)

    def compute_output(self) -> bool:
        if not self.inputs_valid():
            return False
        self.output.signal = self.input_a.signal | self.input_b.signal
        return True

    @property
    def invalid_input_names(self) -> List[str]:
        return super().invalid_input_names


class NotGate(OneInputLogicGate):
    """Not Gate"""

    def __init__(self, input_name, output_name):
        super().__init__(GateType.NOT, input_name, output_name)

    def compute_output(self) -> bool:
        if not self.inputs_valid():
            return False
        self.output.signal = ~self.input.signal
        return True

    @property
    def invalid_input_names(self) -> List[str]:
        return super().invalid_input_names


class LShiftGate(ShiftLogicGate):
    """Left Shift Gate"""

    def __init__(self, input_name, shift_places, output_name):
        super().__init__(GateType.LSHIFT, input_name, shift_places, output_name)

    def compute_output(self) -> bool:
        if not self.inputs_valid():
            return False
        self.output.signal = self.input.signal << self.shift_places
        return True

    @property
    def invalid_input_names(self) -> List[str]:
        return super().invalid_input_names


class RShiftGate(ShiftLogicGate):
    """Right Shift Gate"""

    def __init__(self, input_name, shift_places, output_name):
        super().__init__(GateType.RSHIFT, input_name, shift_places, output_name)

    def compute_output(self) -> bool:
        if not self.inputs_valid():
            return False
        self.output.signal = self.input.signal >> self.shift_places
        return True

    @property
    def invalid_input_names(self) -> List[str]:
        return super().invalid_input_names

def logic_gate_factory(gate_description:GateDescription):
    """Factory Function to return correct gate type"""
    match gate_description.operation:
        case "AND":
            return AndGate(gate_description.input_a,gate_description.input_b,gate_description.output)
        case "OR":
            return OrGate(gate_description.input_a, gate_description.input_b, gate_description.output)
        case "NOT":
            return NotGate(gate_description.input_a, gate_description.output)
        case "LSHIFT":
            return LShiftGate(gate_description.input_a, gate_description.input_b, gate_description.output)
        case "RSHIFT":
            return RShiftGate(gate_description.input_a, gate_description.input_b, gate_description.output)
        case _:
            return DirectGate(gate_description.input_a, gate_description.output)