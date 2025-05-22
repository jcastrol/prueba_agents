from dataclasses import dataclass
from typing import Optional
from typing import List
from datetime import datetime

@dataclass
class SimulationFilterParams:
    agent_id: Optional[str] = None
    event_type: Optional[str] = None
    action: Optional[str] = None
    min_iteration: Optional[int] = None
    max_iteration: Optional[int] = None
    offset: int = 0
    limit: int = 20

@dataclass
class SimulationDetailOutput:
    simulation_id: str
    created_at: datetime
    total_iterations: int
    initial_price: float
    initial_stock: int
    final_stock: int
    final_price: float
    price_history: List[float]
    random_agents: int
    trend_agents: int
    antitrend_agents: int
    smart_agents: int

