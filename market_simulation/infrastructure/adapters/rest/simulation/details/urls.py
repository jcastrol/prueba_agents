from django.urls import path
from market_simulation.infrastructure.adapters.rest.simulation.details.views import (  
    SimulationEventListView,
    TransactionListView,
    SimulationDetailView,
)



urlpatterns = [
    path("<uuid:simulation_id>", SimulationDetailView.as_view(), name="simulation-detail"),
    path("<uuid:simulation_id>/events", SimulationEventListView.as_view(), name="simulation-events"),
    path("<uuid:simulation_id>/transactions", TransactionListView.as_view(), name="simulation-transactions"),
]