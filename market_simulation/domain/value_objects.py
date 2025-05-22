from enum import Enum
from dataclasses import dataclass

class Action(Enum):
    BUY = 'buy'
    SELL = 'sell'
    HOLD = 'hold'

    def __str__(self):
        return self.value
 
    
class MarketRules:
    def __init__(self, buy_impact: float = 0.005, sell_impact: float = 0.005):
        self.buy_impact = buy_impact
        self.sell_impact = sell_impact

    def adjust_price(self, current_price: float, action: Action) -> float:
        if action == Action.BUY:
            return current_price * (1 + self.buy_impact)
        elif action == Action.SELL:
            return current_price * (1 - self.sell_impact)
        return current_price
    

class AgentBalance:
    agent_id: int
    balance: float
    agent_type: str 
    inventory: int


class SimulationConfig:
    
    total_iterations: int
    num_random: int
    num_trend: int
    num_antitrend: int
    num_smart: int = 1
    initial_price: float = 200.0
    initial_stock: int = 100_000