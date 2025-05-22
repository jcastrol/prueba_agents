
class Transaction:
    def __init__(self, agent_id: int, action: str, price: float, iteration: int):
        self.agent_id = agent_id
        self.action = action
        self.price = price
        self.iteration = iteration