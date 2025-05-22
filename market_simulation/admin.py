from django.contrib import admin
from market_simulation.infrastructure.models.simulation import SimulationModel
from market_simulation.infrastructure.models.transaction import TransactionModel
from market_simulation.infrastructure.models.event import EventModel
from market_simulation.infrastructure.models.agent_balance import AgentBalanceModel

admin.site.register(SimulationModel)
admin.site.register(TransactionModel)
admin.site.register(EventModel)
admin.site.register(AgentBalanceModel)