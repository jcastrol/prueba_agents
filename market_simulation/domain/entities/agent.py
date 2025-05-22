
from ..value_objects import Action
from abc import ABC, abstractmethod
import random


class Agent(ABC):
    def __init__(self, agent_id: int, initial_balance: float = 1000.0):
        self.id = agent_id
        self.balance = initial_balance
        self.inventory = 0

    @abstractmethod
    def decide_action(self, *, current_price: float, price_change: float, turn: int, iteration:int) -> Action:
        pass

    def buy(self, price: float) -> bool:
        if self.can_buy(price):
            self.balance -= price
            self.inventory += 1
            return True
        return False

    def sell(self, price: float) -> bool:
        if self.can_sell():
            self.balance += price
            self.inventory -= 1
            return True
        return False

    def can_buy(self, price: float) -> bool:
        return self.balance >= price

    def can_sell(self) -> bool:
        return self.inventory > 0
    
    def get_type(self) -> str:
        return self.__class__.__name__
    

class RandomAgent(Agent):
    def decide_action(self, *, current_price: float, price_change: float, turn: int, iteration:int) -> Action:
        return random.choice([Action.BUY, Action.SELL, Action.HOLD])
    

class TrendFollowerAgent(Agent):
    def decide_action(self, *, current_price: float, price_change: float, turn: int, iteration:int ) -> Action:
        if price_change >= 0.01:
            return random.choices(
                [Action.BUY, Action.HOLD],
                weights=[0.75, 0.25],
                k=1
            )[0]
        else:
            return random.choices(
                [Action.SELL, Action.HOLD],
                weights=[0.20, 0.80],
                k=1
            )[0]
        
class AntiTrendAgent(Agent):
    def decide_action(self, *, current_price: float, price_change: float, turn: int, iteration:int) -> Action:
        if price_change <= -0.01:
            return random.choices(
                [Action.BUY, Action.HOLD],
                weights=[0.75, 0.25],
                k=1
            )[0]
        else:
            return random.choices(
                [Action.SELL, Action.HOLD],
                weights=[0.20, 0.80],
                k=1
            )[0]
        
class MyAgent(Agent):

    def __init__(self, agent_id: int, total_iterations: int, initial_balance: float = 1000.0):
        super().__init__(agent_id, initial_balance)
        self.total_iterations = total_iterations
        self.last_buy_price = 0.0

    def decide_action(self, *, current_price: float, price_change: float, turn: int, iteration:int) -> Action:
        remaining_iterations = self.total_iterations - iteration
        
        #  Liquidar stock
        if remaining_iterations <= self.inventory:
            if self.can_sell():
                return Action.SELL
            else:
                return Action.HOLD
            
        # Compras en etapas tempranas
        if turn < self.total_iterations * 0.006 and price_change < 0.01 and self.can_buy(current_price):
            self.last_buy_price = current_price
            return Action.BUY    
        

        # Estrategia: comprar barato, vender caro
        if price_change < -0.01 and current_price < self.last_buy_price and self.can_buy(current_price):
            self.last_buy_price = current_price
            return Action.BUY

        if price_change > 0.015 and self.can_sell():
            return Action.SELL

        return Action.HOLD