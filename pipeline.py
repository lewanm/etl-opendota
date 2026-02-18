from extract import get_recent_matches, PLAYER_ID
from transform import transform_matches
from load import create_table, load_matches

def run_pipeline():
    print("Iniciando ETL...")

    print("Extrayendo datos desde OpenDota API...")
    df_raw = get_recent_matches(PLAYER_ID)

    print("Transformando datos...")
    df_clean = transform_matches(df_raw)

    print("Creando tabla en MySQL...")
    create_table()

    print("Cargando datos en MySQL...")
    load_matches(df_clean)

    print("ETL completado con exito.")

if __name__ == "__main__":
    run_pipeline()