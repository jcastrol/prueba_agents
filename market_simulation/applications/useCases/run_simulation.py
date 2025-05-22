from typing import List, Dict
from market_simulation.domain.entities.agent import Agent
from market_simulation.domain.entities.market import Market
from market_simulation.applications.ports.agent_creator_port import AgentCreatorPort

from market_simulation.applications.useCases.run_market_iteration import (
    run_market_iteration,
)
from market_simulation.domain.entities.simulation import Simulation
from market_simulation.applications.dtos import AgentBalance, SimulationConfig
from market_simulation.domain.repositories.simulation_repository import (
    SimulationRepository,
)


def run_simulation(
    agent_creator: AgentCreatorPort,
    simulation_repository: SimulationRepository,
    config: SimulationConfig,
) -> Dict:
    all_events = []
    all_transactions = []

    # 1. Crear agentes y mercado
    agents: List[Agent] = agent_creator.create_agents(
        total_iterations=config.total_iterations,
        num_random=config.num_random,
        num_trend=config.num_trend,
        num_antitrend=config.num_antitrend,
        num_smart=config.num_smart,
    )

    market = Market(
        agents=agents,
        initial_price=config.initial_price,
        initial_stock=config.initial_stock,
    )


    # 2. Ejecutar iteraciones del mercado
    for _ in range(config.total_iterations):
        result = run_market_iteration(market)
        all_events.extend(result.events)
        all_transactions.extend(result.transactions)
   
    # 3. Crear lista de balances finales
    agent_balances = [
        AgentBalance(
            agent_id=agent.id,
            agent_type=agent.get_type(),
            balance=agent.balance,
            inventory=agent.inventory,
        )
        for agent in agents
    ]

    # 4. Crear entidad Simulation
    simulation_id = simulation_repository.next_id()
    simulation = Simulation(
        id=simulation_id,
        final_price=market.price,
        final_stock=market.stock,
        price_history=market.price_history,
        transactions=all_transactions,
        events=all_events,
        agent_balances=agent_balances,
    )

    # 5. Guardar la simulación en el repositorio
    simulation_repository.save(simulation, config)

    # 6. Retornar respuesta 
    return {
        "simulation_id": simulation.id,
        "final_price": simulation.final_price,
        "final_stock": simulation.final_stock,
        "price_history": simulation.price_history,
        "agent_balances": [
            {
                "id": b.agent_id,
                "agent_type": b.agent_type,
                "balance": b.balance,
                "inventory": b.inventory,
            }
            for b in agent_balances
        ],
        "total_transactions": len(all_transactions),
        "total_events": len(all_events),
    }
