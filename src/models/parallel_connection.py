from dataclasses import dataclass, field

from .circuit_node import CircuitNode


@dataclass
class ParallelConnection(CircuitNode):
    id: str
    components: list[CircuitNode] = field(default_factory=list)

    def calculate_missing_values(self) -> None:
        if not self.components:
            raise ValueError("Parallel connection must have at least one component.")

        total_reciprocal_resistance = sum(1 / component.get_resistance() for component in self.components)
        self.resistance = 1 / total_reciprocal_resistance

        if self.voltage is not None:
            self.current = sum(component.get_current(self.voltage) for component in self.components)
        elif self.current is not None:
            self.voltage = sum(component.get_voltage(self.current) for component in self.components)
        else:
            raise ValueError("At least one of voltage or current must be provided.")
        