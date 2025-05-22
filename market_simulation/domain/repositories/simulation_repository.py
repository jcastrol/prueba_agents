from abc import ABC, abstractmethod
from ..entities.simulation import Simulation
from ..value_objects import SimulationConfig
from uuid import UUID
from ..dtos import SimulationFilterParams

class SimulationRepository(ABC):
    @abstractmethod
    def save(self, simulation: Simulation,config:SimulationConfig) -> None:
        """Guarda la simulación completa, incluyendo eventos, transacciones y balances"""
        pass
    @abstractmethod
    def next_id(self) -> UUID:
        """Genera un nuevo ID único para la simulación"""
        pass

    @abstractmethod
    def get_with_filtered_events(self, simulation_id: str, filters: SimulationFilterParams) -> list[dict]:
        """Obtiene eventos de la simulación filtrados por los parámetros dados"""
        pass

    @abstractmethod
    def get_with_filtered_transactions(self, simulation_id: str, filters: SimulationFilterParams) -> list[dict]:
        """Obtiene eventos de la simulación filtrados por los parámetros dados"""
        pass
    