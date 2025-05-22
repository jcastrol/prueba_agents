from rest_framework import serializers


class SimulationInputSerializer(serializers.Serializer):
    total_iterations = serializers.IntegerField(min_value=1, default=1000)
    random_agents = serializers.IntegerField(min_value=0, default=51)
    trend_agents = serializers.IntegerField(min_value=0, default=24)
    antitrend_agents = serializers.IntegerField(min_value=0, default=24)
    smart_agents = serializers.IntegerField(min_value=0, default=1)
    initial_price = serializers.FloatField(min_value=0.01, default=200.0)
    initial_stock = serializers.IntegerField(min_value=1, default=100_000)

    def validate(self, data):
        total_agents = (
            data.get("random_agents", 0)
            + data.get("trend_agents", 0)
            + data.get("antitrend_agents", 0)
            + data.get("smart_agents", 0)
        )
        if total_agents != 100:
            raise serializers.ValidationError(
                f"La suma total de agentes debe ser 100. Actualmente: {total_agents}."
            )
        return data


class AgentBalanceSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    balance = serializers.FloatField()
    agent_type = serializers.CharField()
    inventory = serializers.IntegerField()


class SimulationEventSerializer(serializers.Serializer):
    name = serializers.CharField()
    payload = serializers.DictField()

class TransactionSerializer(serializers.Serializer):
    agent_id = serializers.IntegerField()
    action = serializers.CharField()
    price = serializers.FloatField()
    iteration = serializers.IntegerField()

    
class SimulationOutputSerializer(serializers.Serializer):
    simulation_id = serializers.UUIDField()
    final_price = serializers.FloatField()
    final_stock = serializers.IntegerField()
    total_transactions = serializers.IntegerField()
    total_events = serializers.IntegerField()
    price_history = serializers.ListField(child=serializers.FloatField())
    agent_balances = AgentBalanceSerializer(many=True)


class SimulationDetailSerializer(serializers.Serializer):
    simulation_id = serializers.UUIDField()
    created_at = serializers.DateTimeField()
    total_iterations = serializers.IntegerField()
    initial_price = serializers.FloatField()
    initial_stock = serializers.IntegerField()
    final_price = serializers.FloatField()
    price_history = serializers.ListField(child=serializers.FloatField())
    random_agents = serializers.IntegerField()
    trend_agents = serializers.IntegerField()
    antitrend_agents = serializers.IntegerField()
    smart_agents = serializers.IntegerField()