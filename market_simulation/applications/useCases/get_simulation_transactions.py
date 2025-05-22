from typing import List
from market_simulation.domain.repositories.simulation_repository import SimulationRepository 
from market_simulation.domain.dtos import SimulationFilterParams

def get_simulation_transactions(
    repository: SimulationRepository, simulation_id: str, filters: SimulationFilterParams
) -> List[dict]:
    return repository.get_with_filtered_transactions(simulation_id, filters)