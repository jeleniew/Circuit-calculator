from dataclasses import dataclass, field

from .circuit_node import CircuitNode

@dataclass
class SeriesConnection(CircuitNode):
    id: str
    components: list["CircuitNode"] = field(default_factory=list)

    def calculate_missing_values(self):
        if not self.components:
            raise ValueError("Series connection must have at least one component.")

        self.resistance = sum(component.get_resistance() for component in self.components)

        if self.voltage is not None:
            self.current = self.voltage / self.resistance
        elif self.current is not None:
            self.voltage = self.current * self.resistance
        else:
            raise ValueError("At least one of voltage or current must be provided.")