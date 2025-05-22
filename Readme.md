#  Simulator Market Test API

Este proyecto se basa en una economía simulada basada en el intercambio de tarjetas gráficas, en la que múltiples agentes interactúan bajo distintas estrategias y reglas definidas por defecto. Se ha diseñado para que la simulación sea completamente parametrizable, permitiendo ajustar variables clave como el número de iteraciones,cantidad de tipos de agentes, precios y stock iniciales. Además, todas las transacciones y eventos generados durante la simulación se registran en una base de datos, lo que facilita su análisis posterior o exportación a otras herramientas analíticas.

El desarrollo se ha realizado utilizando Django y Django REST Framework, aplicando principios de arquitectura limpia como Domain-Driven Design (DDD) y arquitectura hexagonal para asegurar una separación clara de responsabilidades.

## Características

- API REST para ejecutar y consultar simulaciones.
- Simulación de mercado con agentes de comportamiento definido.
- Agentes disponibles: aleatorios, tendenciales, antitendenciales, personalizados.
- transacciones por iteración y Persistencia de eventos.
- Paginación y filtros en endpoints de consulta.
- Documentación automática con Swagger y drf-spectacular.


## Arquitectura del Proyecto

El proyecto está estructurado de forma modular, basada en los principios de Clean Architecture y Domain-Driven Design (DDD).

- `market_simulation/domain/`: Entidades de dominio, values_objet, y repositories.
- `market_simulation/applications/`: Casos de uso que orquestan la lógica de negocio y ports.
- `market_simulation/infrastructure/`: Repositorios, ORM y adaptadores de entrada/salida.

## Instalación y Configuración

```bash
git clone https://github.com/tu_usuario/market-simulation.git
cd market-simulation
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Migraciones y Base de Datos

```bash
python manage.py makemigrations
python manage.py migrate
```


## Ejecución

### Iniciar servidor

```bash
python manage.py runserver
```

### Ejecutar pruebas

```bash
pytest
```


## Endpoints Principales

### POST `/api/simulation/`

Ejecuta una simulación. Acepta parámetros personalizados o usa valores por defecto.

#### Payload ejemplo
```json
{
  ""total_iterations"": 1000,
  ""random_agents"": 50,
  ""trend_agents"": 25,
  ""antitrend_agents"": 25,
  ""smart_agents"": 0,
  ""initial_price"": 200.0,
  ""initial_stock"": 100000
}
```

### GET `/api/simulation/<simulation_id>/`

Retorna los datos generales de la simulación, precio final, configuración inicial y balances de agentes.

### GET `/api/simulation/<simulation_id>/transactions/`

Listado paginado de transacciones de la simulacion. Filtros opcionales:
- `agent_id`
- `action`: BUY / SELL
- `min_iteration`
- `max_iteration`
- `page`

### GET `/api/simulation/<simulation_id>/events/`

Listado paginado de eventos de la simulacion. Filtros opcionales:
- `agent_id`
- `event_type`
- `min_iteration`
- `max_iteration`
- `page`


## Documentación

Una vez el servidor esté activo, accede a la documentación Swagger:

```
http://localhost:8000/api/schema/swagger-ui/
```

Autor

Desarrollado por [Jhonny Castro Lopez / GitHub](https://github.com/jcastrol)