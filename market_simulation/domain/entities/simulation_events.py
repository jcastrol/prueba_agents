from dataclasses import dataclass
from datetime import datetime
from market_simulation.domain.events import DomainEvent


class SimulationEvent:
    id: int
    simulation_id: int
    agent_id: int
    event_type: str
    payload: dict
    iteration: int
    timestamp: datetime