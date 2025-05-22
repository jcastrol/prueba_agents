from rest_framework import serializers


class SimulationEventSerializer(serializers.Serializer):
    # name = serializers.CharField()
    payload = serializers.JSONField()
    iteration = serializers.IntegerField()
    agent_id = serializers.IntegerField()
    simulation_id = serializers.UUIDField()
    event_type = serializers.CharField()
    timestamp = serializers.DateTimeField()

class TransactionSerializer(serializers.Serializer):
    agent_id = serializers.IntegerField()
    action = serializers.CharField()
    price = serializers.FloatField()
    iteration = serializers.IntegerField()
    simulation_id = serializers.UUIDField()
    timestamp = serializers.DateTimeField()

class SimulationDetailOutputSerializer(serializers.Serializer):
    simulation_id = serializers.CharField()
    final_price = serializers.FloatField()
    final_stock = serializers.IntegerField()
    initial_price = serializers.FloatField()
    initial_stock = serializers.IntegerField()
    total_iterations = serializers.IntegerField()
    created_at = serializers.DateTimeField()
    price_history = serializers.ListField(child=serializers.FloatField())
    