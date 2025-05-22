from django.db import models
from market_simulation.infrastructure.models.simulation import SimulationModel

class EventModel(models.Model):
    id = models.AutoField(primary_key=True)
    simulation = models.ForeignKey(SimulationModel, on_delete=models.CASCADE, related_name="events")
    agent_id = models.IntegerField()
    event_type = models.CharField(max_length=50)
    payload = models.JSONField()
    iteration = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Event {self.event_type} - Agent {self.agent_id}"
