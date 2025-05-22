from market_simulation.domain.repositories.simulation_repository import SimulationRepository
from market_simulation.domain.dtos import SimulationDetailOutput


def get_simulation_detail(simulation_repo: SimulationRepository, simulation_id: str) -> SimulationDetailOutput:
    return simulation_repo.get_by_id(simulation_id)