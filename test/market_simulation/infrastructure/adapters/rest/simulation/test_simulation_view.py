import pytest
from rest_framework.test import APIClient
from rest_framework import status
from market_simulation.domain.value_objects import Action

@pytest.mark.django_db
class TestSimulationEndpoint:

    def setup_method(self):
        self.client = APIClient()
        self.url = "/api/simulation/"

    def test_simulation_with_defaults(self):
        response = self.client.post(self.url, {})
        assert response.status_code == status.HTTP_200_OK
        data = response.data

        assert "simulation_id" in data
        assert isinstance(data["simulation_id"], str)

        assert "final_price" in data
        assert isinstance(data["final_price"], float)

        assert "price_history" in data
        assert isinstance(data["price_history"], list)
        assert all(isinstance(p, float) for p in data["price_history"])

        assert "agent_balances" in data
        assert isinstance(data["agent_balances"], list)
        assert len(data["agent_balances"]) == 100

        assert "total_transactions" in data
        assert isinstance(data["total_transactions"], int)

        assert "total_events" in data
        assert isinstance(data["total_events"], int)
        

    def test_simulation_with_custom_config(self):
        payload = {
            "total_iterations": 500,
            "random_agents": 40,
            "trend_agents": 30,
            "antitrend_agents": 29,
            "smart_agents": 1,
            "initial_price": 150.0,
            "initial_stock": 50000
        }
        response = self.client.post(self.url, payload)
        assert response.status_code == status.HTTP_200_OK
        data = response.data
        assert "simulation_id" in data
        assert isinstance(data["simulation_id"], str)

        assert "final_price" in data
        assert isinstance(data["final_price"], float)
        assert data["final_price"] > 0

        assert "price_history" in data
        assert isinstance(data["price_history"], list)

        assert "agent_balances" in data
        assert isinstance(data["agent_balances"], list)
        assert len(data["agent_balances"]) == 100

        assert "total_transactions" in data
        assert isinstance(data["total_transactions"], int)

        assert "total_events" in data
        assert isinstance(data["total_events"], int)

    def test_invalid_agent_sum(self):
        payload = {
            "total_iterations": 500,
            "random_agents": 40,
            "trend_agents": 30,
            "antitrend_agents": 29,
            "smart_agents": 2  # Total = 101
        }
        response = self.client.post(self.url, payload)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "La suma total de agentes debe ser 100" in str(response.data)

    def test_missing_required_fields(self):
        payload = {
            "random_agents": 50,
            "trend_agents": 25,
            "antitrend_agents": 25,
            "smart_agents": 0  # explícito para que total = 100
        }
        response = self.client.post(self.url, payload)
        assert response.status_code == status.HTTP_200_OK