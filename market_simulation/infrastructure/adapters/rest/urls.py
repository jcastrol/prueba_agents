
from django.urls import path, include

urlpatterns = [
    path("simulation/", include("market_simulation.infrastructure.adapters.rest.simulation.urls")),
]
