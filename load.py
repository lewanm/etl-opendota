import mysql.connector 
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()

def create_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=os.getenv("MYSQL_DATABASE")
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def create_table():
    query = """
    CREATE TABLE IF NOT EXISTS matches(
        match_id BIGINT PRIMARY KEY,
        hero_id INT,
        kills INT,
        deaths INT,
        assists INT,
        kda FLOAT,
        duration_minutes FLOAT
    );
    """

    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()


def load_matches(df):
    conn = create_connection()
    if conn:
        cursor = conn.cursor()  

        insert_query = """
        REPLACE INTO matches (match_id, hero_id, kills, deaths, assists, kda,duration_minutes)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        for _, row in df.iterrows():
            cursor.execute(insert_query, tuple(row))

        conn.commit()
        cursor.close()
        conn.close()
        print("Datos cargados correctamente en MySQL.")

