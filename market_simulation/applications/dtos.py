from dataclasses import dataclass
from typing import List
from market_simulation.domain.entities.transaction import Transaction
from market_simulation.domain.events import DomainEvent


@dataclass
class MarketIterationResult:
    transactions: List[Transaction]
    events: List[DomainEvent]

@dataclass
class AgentBalance:
    agent_id: int
    balance: float
    agent_type: str 
    inventory: int

@dataclass(frozen=True)
class SimulationConfig:
    
    total_iterations: int
    num_random: int 
    num_trend: int 
    num_antitrend: int 
    num_smart: int 
    initial_price: float 
    initial_stock: int 