import random
from typing import List, Optional
from .agent import Agent
from ..value_objects import MarketRules


class Market:
    def __init__(
        self,
        agents: List[Agent],
        initial_price: float = 200.0,
        initial_stock: int = 100_000,
        rules: Optional[MarketRules] = None
    ):
        self.agents = agents
        self.price = initial_price
        self.stock = initial_stock
        self.iteration = 0
        self.price_history = [initial_price]
        self.rules = rules or MarketRules()

    

    def _shuffle_agents(self) -> List[Agent]:
        agents_copy = self.agents[:]
        random.shuffle(agents_copy)
        return agents_copy