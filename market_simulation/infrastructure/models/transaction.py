from django.db import models
from market_simulation.infrastructure.models.simulation import SimulationModel

class TransactionModel(models.Model):
    ACTION_CHOICES = [
        ("BUY", "Buy"),
        ("SELL", "Sell"),
    ]

    id = models.AutoField(primary_key=True)
    simulation = models.ForeignKey(SimulationModel, on_delete=models.CASCADE, related_name="transactions")
    agent_id = models.IntegerField()
    action = models.CharField(max_length=4, choices=ACTION_CHOICES)
    price = models.FloatField()
    iteration = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.action} by Agent {self.agent_id} @ {self.price}"
