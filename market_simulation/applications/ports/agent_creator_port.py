from abc import ABC, abstractmethod
from typing import List
from market_simulation.domain.entities.agent import Agent


class AgentCreatorPort(ABC):
    @abstractmethod
    def create_agents(
        self,
        total_iterations: int,
        num_random: int,
        num_trend: int,
        num_antitrend: int,
        num_smart: int
    ) -> List[Agent]:
        pass