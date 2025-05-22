from typing import Optional, Tuple
from market_simulation.domain.entities.agent import Agent
from market_simulation.domain.value_objects import MarketRules
from market_simulation.domain.value_objects import Action
from market_simulation.domain.entities.transaction import Transaction
from market_simulation.domain.events import  DomainEvent, AgentBoughtCard, AgentSoldCard, AgentHeldPosition


def process_agent_turn(
    agent: Agent,
    current_price: float,
    price_change: float,
    turn: int,
    stock: int,
    rules: MarketRules,
    iteration: int,
) -> Tuple[Action, bool, float, int, Optional[Transaction], DomainEvent]:

    action = agent.decide_action(
        current_price=current_price,
        price_change=price_change,
        turn=turn,
        iteration=iteration
    )

    price = current_price
    stock_update = stock
    applied = False
    transaction = None
    event: DomainEvent

    if action == Action.BUY and stock > 0 and agent.can_buy(price):
        if agent.buy(price):
            stock_update -= 1
            price = rules.adjust_price(price, Action.BUY)
            applied = True
            transaction = Transaction(
                agent_id=agent.id,
                action=Action.BUY,
                price=price,
                iteration=iteration
            )
            event = AgentBoughtCard(agent_id=agent.id, price=price, iteration=iteration)

    elif action == Action.SELL and agent.can_sell():
        if agent.sell(price):
            stock_update += 1
            price = rules.adjust_price(price, Action.SELL)
            applied = True
            transaction = Transaction(
                agent_id=agent.id,
                action=Action.SELL,
                price=price,
                iteration=iteration
            )
            event = AgentSoldCard(agent_id=agent.id, price=price, iteration=iteration)

    else:
        # HOLD
        event = AgentHeldPosition(agent_id=agent.id, iteration=iteration)

    return action, applied, price, stock_update, transaction, event