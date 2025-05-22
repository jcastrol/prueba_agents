from dataclasses import dataclass


@dataclass(frozen=True)
class DomainEvent:
    name: str
    payload: dict


@dataclass(frozen=True)
class AgentBoughtCard(DomainEvent):
    def __init__(self, agent_id: int, price: float, iteration: int):
        super().__init__(
            name="AgentBoughtCard",
            payload={"agent_id": agent_id, "price": price, "iteration": iteration},
        )


@dataclass(frozen=True)
class AgentSoldCard(DomainEvent):
    def __init__(self, agent_id: int, price: float, iteration: int):
        super().__init__(
            name="AgentSoldCard",
            payload={"agent_id": agent_id, "price": price, "iteration": iteration},
        )


@dataclass(frozen=True)
class AgentHeldPosition(DomainEvent):
    def __init__(self, agent_id: int, iteration: int):
        super().__init__(
            name="AgentHeldPosition",
            payload={"agent_id": agent_id, "iteration": iteration},
        )