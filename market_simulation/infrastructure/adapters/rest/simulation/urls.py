from django.urls import path,include
from .views import SimulationView

urlpatterns = [
    path("", SimulationView.as_view(), name="run-simulation"),
    path("", include("market_simulation.infrastructure.adapters.rest.simulation.details.urls")),
]