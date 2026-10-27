from abc import ABC, abstractmethod


class CircuitNode(ABC):
    resistance: float | None
    voltage: float | None
    current: float | None

    def get_resistance(self) -> float:
        return self.resistance
    
    def get_voltage(self) -> float:
        return self.voltage

    def get_current(self) -> float:
        return self.current

    @abstractmethod
    def calculate_missing_values(self) -> None:
        pass