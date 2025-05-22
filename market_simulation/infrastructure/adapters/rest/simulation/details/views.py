from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiParameter
from market_simulation.infrastructure.adapters.rest.simulation.details.serializers import SimulationDetailOutputSerializer
from market_simulation.applications.useCases.get_simulation_detail import get_simulation_detail

from market_simulation.infrastructure.adapters.rest.simulation.serializers import TransactionSerializer
from market_simulation.infrastructure.adapters.rest.simulation.pagination import SimulationPagination

from market_simulation.infrastructure.adapters.rest.simulation.details.serializers import SimulationEventSerializer

from market_simulation.infrastructure.repositories.simulation_repository import DjangoSimulationRepository
from market_simulation.applications.useCases.get_simulation_events import get_simulation_events
from market_simulation.applications.useCases.get_simulation_transactions import get_simulation_transactions
from market_simulation.domain.dtos import SimulationFilterParams

@extend_schema(
    responses={200: SimulationDetailOutputSerializer},
    description="Devuelve los detalles generales de una simulación, incluyendo configuraciones iniciales y un resumen de los resultados finales.",
    tags=["Simulación"],
    operation_id="get_simulation_detail"
)
class SimulationDetailView(APIView):
    def get(self, request, simulation_id):
        repo = DjangoSimulationRepository()
        detail = get_simulation_detail(repo, simulation_id)
        serializer = SimulationDetailOutputSerializer(detail)
        return Response(serializer.data, status=status.HTTP_200_OK)


@extend_schema(
    parameters=[
        OpenApiParameter(name="agent_id", type=str, required=False, description="Filtra por ID del agente."),
        OpenApiParameter(name="event_type", type=str, required=False, description="Filtra por tipo de evento."),
        OpenApiParameter(name="min_iteration", type=int, required=False, description="Filtra eventos desde esta iteración."),
        OpenApiParameter(name="max_iteration", type=int, required=False, description="Filtra eventos hasta esta iteración."),
        OpenApiParameter(name="page", type=int, required=False, description="Número de página para paginación."),
    ],
    responses={200: SimulationEventSerializer(many=True)},
    description="Lista paginada de eventos generados durante la simulación. Permite aplicar filtros por agente, tipo de evento y rango de iteraciones.",
    tags=["Simulación"],
    operation_id="get_simulation_events"
)
class SimulationEventListView(ListAPIView):
    serializer_class = SimulationEventSerializer
    pagination_class = SimulationPagination

    def get_queryset(self):
        simulation_id = self.kwargs["simulation_id"]
        params = self.request.query_params

        filters = SimulationFilterParams(
            agent_id=params.get("agent_id"),
            event_type=params.get("event_type"),
            min_iteration=int(params["min_iteration"]) if "min_iteration" in params else None,
            max_iteration=int(params["max_iteration"]) if "max_iteration" in params else None,
           
        )

        repo = DjangoSimulationRepository()
        events = get_simulation_events(repo, simulation_id, filters)

        return events


@extend_schema(
    parameters=[
        OpenApiParameter(name="agent_id", type=str, required=False, description="Filtra por ID del agente."),
        OpenApiParameter(name="action", type=str, required=False, description="Filtra por tipo de acción (BUY / SELL)."),
        OpenApiParameter(name="min_iteration", type=int, required=False, description="Filtra transacciones desde esta iteración."),
        OpenApiParameter(name="max_iteration", type=int, required=False, description="Filtra transacciones hasta esta iteración."),
        OpenApiParameter(name="page", type=int, required=False, description="Número de página para paginación."),
    ],
    responses={200: TransactionSerializer(many=True)},
    description="Lista paginada de transacciones generadas durante la simulación. Permite aplicar filtros por agente, tipo de acción y rango de iteraciones.",
    tags=["Simulación"],
    operation_id="get_simulation_transactions"
)
class TransactionListView(ListAPIView):
    serializer_class = TransactionSerializer
    pagination_class = SimulationPagination

    def get_queryset(self):
            
        simulation_id = self.kwargs["simulation_id"]
        params = self.request.query_params

        filters = SimulationFilterParams(
            agent_id=params.get("agent_id"),
            action=params.get("action"),
            min_iteration=int(params["min_iteration"]) if "min_iteration" in params else None,
            max_iteration=int(params["max_iteration"]) if "max_iteration" in params else None,
           
        )

        repo = DjangoSimulationRepository()
        transactions = get_simulation_transactions(repo, simulation_id, filters)

        return transactions