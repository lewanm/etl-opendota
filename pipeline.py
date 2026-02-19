import sys
from extract import get_recent_matches
from transform import transform_matches
from load import create_table, load_matches

def run_pipeline(player_id=None):
    print("Iniciando ETL...")

    print("Extrayendo datos desde OpenDota API...")
    df_raw = get_recent_matches(player_id)
    print("Transformando datos...")
    df_clean = transform_matches(df_raw)

    print("Creando tabla en MySQL...")
    create_table()

    print("Cargando datos en MySQL...")
    load_matches(df_clean)

    print("ETL completado con exito.")

if __name__ == "__main__":
    player_id = sys.argv[1] if len(sys.argv) > 1 else None
    run_pipeline(player_id) 