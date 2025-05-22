from typing import List
from ..value_objects import AgentBalance
from .transaction import Transaction
from ..events import DomainEvent

class Simulation:
    def __init__(
        self,
        id: int,
        final_price: float,
        final_stock: int,
        price_history: List[float],
        transactions: List[Transaction],
        events: List[DomainEvent],
        agent_balances: List[AgentBalance],
    ):
        self.id = id
        self.final_price = final_price
        self.final_stock = final_stock
        self.price_history = price_history
        self.transactions = transactions
        self.events = events
        self.agent_balances = agent_balances
