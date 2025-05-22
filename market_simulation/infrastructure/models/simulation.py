from django.db import models
import uuid

class SimulationModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    total_iterations = models.IntegerField()
    initial_price = models.FloatField()
    initial_stock = models.IntegerField()
    final_stock = models.IntegerField( default=0)
    final_price = models.FloatField( default=0.0)
    price_history = models.JSONField(default=list)

    random_agents = models.IntegerField()
    trend_agents = models.IntegerField()
    antitrend_agents = models.IntegerField()
    smart_agents = models.IntegerField()

    def __str__(self):
        return f"Simulation #{self.id} - {self.created_at.date()}"

