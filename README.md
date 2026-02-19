# ETL Pipeline con OpenDota API (Python + Pandas + MySQL)

Este proyecto implementa un pipeline ETL completo para obtener, transformar y almacenar datos reales de partidas de Dota 2 utilizando la API pública de **OpenDota**.  
Incluye extracción desde API REST, transformación con Python/Pandas, carga en MySQL y un dashboard interactivo en Streamlit para visualizar métricas del jugador.

---

## Características principales

- **Extracción de datos** desde la API pública de OpenDota.
- **Transformación**: limpieza, normalización, cálculo de métricas (KDA, duración, winrate).
- **Carga en MySQL** con control de duplicados e inserciones idempotentes.
- **Automatización** mediante scripts modulares.
- **Manejo de errores**: perfiles privados, respuestas vacías, fallos de red.
- **Dashboard en Streamlit** para visualizar estadísticas del jugador.
- **Versionado con Git** y estructura clara del proyecto.

---

## Estructura del proyecto

etl-opendota/
- extract.py        # Lógica de extracción desde OpenDota API
- transform.py      # Limpieza y transformación de datos
- load.py           # Inserción en MySQL
- pipeline.py       # Orquestación del ETL
- dashboard.py      # Dashboard en Streamlit
- requirements.txt  # Dependencias del proyecto
- .env.example      # Variables de entorno

---

## Requisitos

- Python 3.10+
- MySQL Server
- Entorno virtual recomendado

---

## Instalar dependencias:
bash:
```pip install -r requirements.txt```

Configuración
```Crear un archivo .env basado en .env.example:```

Ejecución del pipeline
Ejecutar el ETL completo:
```python pipeline.py 86745912```

Dashboard (Streamlit)
Para visualizar métricas del jugador:
```streamlit run dashboard.py```

## Manejo de errores
El pipeline detecta:

- Perfiles privados

- Jugadores sin partidas públicas

- Respuestas vacías de la API

- Fallos de conexión

_En esos casos, se muestra un mensaje claro y el proceso finaliza sin romperse._

Ejemplo de endpoint utilizado
```https://api.opendota.com/api/players/<PLAYER_ID>/recentMatches```
