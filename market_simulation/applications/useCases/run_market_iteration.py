from market_simulation.applications.dtos import MarketIterationResult
from market_simulation.domain.entities.market import Market
from market_simulation.applications.useCases.process_agent_turn import process_agent_turn
import random

def run_market_iteration(market: Market) -> MarketIterationResult:
    
    market.iteration += 1
    previous_price = market.price
    transactions = []
    events = []

    agents_this_turn = market.agents[:]
    random.shuffle(agents_this_turn)

    for idx, agent in enumerate(agents_this_turn):
        price_change = (market.price - previous_price) / previous_price

        _, _, new_price, new_stock, transaction, event = process_agent_turn(
            agent=agent,
            current_price=market.price,
            price_change=price_change,
            turn=idx,
            stock=market.stock,
            rules=market.rules,
            iteration=market.iteration,
        )

        market.price = new_price
        market.stock = new_stock

        if transaction:
            transactions.append(transaction)
        if event:
            events.append(event)

    market.price_history.append(market.price)

    return MarketIterationResult(
        transactions=transactions,
        events=events
    )
