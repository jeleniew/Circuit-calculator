from abc import ABC, abstractmethod
from collections.abc import Callable

from src.models.circuit_node import CircuitNode

class IMainWindow(ABC):

    @abstractmethod
    def set_calculate_callback(
        self,
        callback: Callable[[], None]
    ) -> None:
        """Register the callback invoked when calculation is requested."""
        pass

    @abstractmethod
    def get_circuit(self) -> CircuitNode:
        """Return the circuit entered by the user."""
        pass

    @abstractmethod
    def show_result(self, resistance: float) -> None:
        """Display the calculated equivalent resistance."""
        pass

    @abstractmethod
    def show_error(self, message: str) -> None:
        """Display an error message."""
        pass