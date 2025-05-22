from django.db import models
from market_simulation.infrastructure.models.simulation import SimulationModel

class AgentBalanceModel(models.Model):
    simulation = models.ForeignKey(SimulationModel, on_delete=models.CASCADE, related_name="agent_balances")
    agent_id = models.IntegerField()
    agent_type = models.CharField(max_length=50)
    balance = models.FloatField()
    inventory = models.IntegerField()

    def __str__(self):
        return f"Agent {self.agent_id} - {self.agent_type}"