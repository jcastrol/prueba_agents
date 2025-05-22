from market_simulation.domain.repositories.simulation_repository import SimulationRepository
from market_simulation.domain.entities.simulation import Simulation
from market_simulation.infrastructure.models.simulation import SimulationModel
from market_simulation.infrastructure.models.transaction import TransactionModel
from market_simulation.infrastructure.models.event import EventModel
from market_simulation.infrastructure.models.agent_balance import AgentBalanceModel
from market_simulation.applications.dtos import SimulationConfig
from market_simulation.domain.dtos import SimulationFilterParams ,SimulationDetailOutput

from uuid import UUID
import uuid


class DjangoSimulationRepository(SimulationRepository):
    def next_id(self) -> UUID:
        return uuid.uuid4()
    
    def save(self, simulation: Simulation, config:SimulationConfig) -> None:
        sim_model = SimulationModel.objects.create(
            id=simulation.id,
            final_price=simulation.final_price,
            price_history=simulation.price_history,
            initial_price=config.initial_price,
            initial_stock=config.initial_stock,
            final_stock=simulation.final_stock,
            total_iterations=config.total_iterations,
            random_agents=config.num_random,
            trend_agents=config.num_trend,
            antitrend_agents=config.num_antitrend,
            smart_agents=config.num_smart,

        )

        # Guardar transacciones
        TransactionModel.objects.bulk_create([
            TransactionModel(
                simulation=sim_model,
                agent_id=t.agent_id,
                action=t.action.value,
                price=t.price,
                iteration=t.iteration,
            ) for t in simulation.transactions
        ])

        # Guardar eventos
        EventModel.objects.bulk_create([
            EventModel(
                simulation=sim_model,
                agent_id=e.payload["agent_id"],
                event_type=e.name,
                payload=e.payload,
                iteration=e.payload["iteration"],
            ) for e in simulation.events
        ])

        # Guardar balances
        AgentBalanceModel.objects.bulk_create([
            AgentBalanceModel(
                simulation=sim_model,
                agent_id=b.agent_id,
                agent_type=b.agent_type,
                balance=b.balance,
                inventory=b.inventory,
            ) for b in simulation.agent_balances
        ])


    def get_with_filtered_events(self, simulation_id: str, filters: SimulationFilterParams) -> list[dict]:
        queryset = EventModel.objects.filter(simulation_id=simulation_id)

        if filters.agent_id:
            queryset = queryset.filter(agent_id=filters.agent_id)
        if filters.event_type:
            queryset = queryset.filter(event_type=filters.event_type)
        if filters.min_iteration is not None:
            queryset = queryset.filter(iteration__gte=filters.min_iteration)
        if filters.max_iteration is not None:
            queryset = queryset.filter(iteration__lte=filters.max_iteration)

        queryset = queryset.order_by("iteration")

        return queryset.values()

    def get_with_filtered_transactions(self, simulation_id: str, filters: SimulationFilterParams) -> list[dict]:
        queryset = TransactionModel.objects.filter(simulation_id=simulation_id)
        print(filters.action)   
        if filters.agent_id:
            queryset = queryset.filter(agent_id=filters.agent_id)
        if filters.action:
            queryset = queryset.filter(action=filters.action)
        if filters.min_iteration is not None:
            queryset = queryset.filter(iteration__gte=filters.min_iteration)
        if filters.max_iteration is not None:
            queryset = queryset.filter(iteration__lte=filters.max_iteration)

        queryset = queryset.order_by("iteration")

        return queryset.values()
    

    def get_by_id(self, simulation_id: str) -> SimulationDetailOutput:
        obj = SimulationModel.objects.get(id=simulation_id)
         
        return SimulationDetailOutput(
            simulation_id=str(obj.id),
            created_at=obj.created_at,
            total_iterations=obj.total_iterations,
            initial_price=obj.initial_price,
            initial_stock=obj.initial_stock,
            final_price=obj.final_price,
            final_stock=obj.final_stock,
            price_history=obj.price_history,
            random_agents=obj.random_agents,
            trend_agents=obj.trend_agents,
            antitrend_agents=obj.antitrend_agents,
            smart_agents=obj.smart_agents,
        )