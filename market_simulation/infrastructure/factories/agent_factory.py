from typing import List
from market_simulation.applications.ports.agent_creator_port import AgentCreatorPort
from market_simulation.domain.entities.agent import (
    Agent,
    RandomAgent,
    TrendFollowerAgent,
    AntiTrendAgent,
    MyAgent,
)
 
class AgentFactory(AgentCreatorPort):
    def create_agents(
        self,
        total_iterations: int,
        num_random: int = 51,
        num_trend: int = 24,
        num_antitrend: int = 24,
        num_smart: int = 1,
    ) -> List[Agent]:
        agents: List[Agent] = []
        agent_id = 0

        for _ in range(num_random):
            agents.append(RandomAgent(agent_id))
            agent_id += 1

        for _ in range(num_trend):
            agents.append(TrendFollowerAgent(agent_id))
            agent_id += 1

        for _ in range(num_antitrend):
            agents.append(AntiTrendAgent(agent_id))
            agent_id += 1

        for _ in range(num_smart):
            agents.append(MyAgent(agent_id, total_iterations))
            agent_id += 1

        return agents