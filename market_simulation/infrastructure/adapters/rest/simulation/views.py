from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiResponse

from market_simulation.applications.dtos import SimulationConfig
from market_simulation.applications.useCases.run_simulation import run_simulation
from market_simulation.infrastructure.factories.agent_factory import AgentFactory
from market_simulation.infrastructure.repositories.simulation_repository import (
    DjangoSimulationRepository,
)
from .serializers import SimulationInputSerializer, SimulationOutputSerializer




@extend_schema(
    request=SimulationInputSerializer,
    responses={
        200: SimulationOutputSerializer,
        400: OpenApiResponse(description="Solicitud inválida. Revisar los parámetros."),
    },
    description=(
        "Esta api ejecuta una simulación del mercado con los parámetros proporcionados.\n\n"
        "Si no se envían parámetros, se utilizan los valores por defecto:\n"
        "- `total_iterations`: 1000\n"
        "- `initial_price`: 200.0\n"
        "- `initial_stock`: 100000\n"
        "- `random_agents`: 51\n"
        "- `trend_agents`: 24\n"
        "- `antitrend_agents`: 24\n"
        "- `smart_agents`: 1\n\n"
        "Retorna el precio final, historial de precios, balances de los agentes y estadísticas generales."
    ),
    tags=["Simulación"],
    operation_id="run_simulation"
)

class SimulationView(APIView):
    def post(self, request):
        serializer = SimulationInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        factory = AgentFactory()
        repository = DjangoSimulationRepository()
        config = SimulationConfig(
            total_iterations=int(data.get("total_iterations", 1000)),
            initial_price=float(data.get("initial_price", 200.0)),
            initial_stock=int(data.get("initial_stock", 100000)),
            num_random=int(data.get("random_agents", 51)),
            num_trend=int(data.get("trend_agents", 24)),
            num_antitrend=int(data.get("antitrend_agents", 24)),
            num_smart=int(data.get("smart_agents", 1)),
        )

        result = run_simulation(
            agent_creator=factory,
            simulation_repository=repository,
            config=config,
        )

        output_serializer = SimulationOutputSerializer(result)
        return Response(output_serializer.data, status=status.HTTP_200_OK)
