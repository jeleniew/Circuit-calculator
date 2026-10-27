from dataclasses import dataclass

from .circuit_node import CircuitNode


@dataclass
class Resistor(CircuitNode):
    id: str

    def __post_init__(self) -> None:
        if self.resistance <= 0:
            raise ValueError("Resistance must be greater than zero.")
        if self.voltage < 0:
            raise ValueError("Voltage cannot be negative.")
        if self.current < 0:
            raise ValueError("Current cannot be negative.")

        self.calculate_missing_values()

    def calculate_missing_values(self) -> None:
        if self.resistance is not None and self.current is not None:
            self.voltage = self.resistance * self.current
        elif self.resistance is not None and self.voltage is not None:
            self.current = self.voltage / self.resistance
        elif self.voltage is not None and self.current is not None:
            self.resistance = self.voltage / self.current
        else:
            raise ValueError("At least two of resistance, voltage, or current must be provided.")