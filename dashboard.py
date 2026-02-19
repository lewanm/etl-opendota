import streamlit as st
import pandas as pd
import mysql.connector
import plotly.express as px
from dotenv import load_dotenv
import os

load_dotenv()


def get_data():
    conn = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE")
    )
    query = "SELECT * FROM matches"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

st.set_page_config(page_title="Dota 2 Dashborad", layout="wide")

st.title("Dashboard de OpenDota - ETL")

df = get_data()

st.subheader("Vista general de los datos")
st.dataframe(df, use_container_width=True)

st.subheader("KDA promedio por heroe")

kda_por_heroe = df.groupby("hero_id")["kda"].mean().reset_index().sort_values(by="kda", ascending=False)

fig_kda = px.bar(
    kda_por_heroe,
    x="kda",
    y="hero_id",
    orientation="h",
    title="KDA Promedio por heroe (ordenado)",
    labels={"hero_id": "Hero ID", "kda": "KDA Promedio"},
    color="kda",
    color_continuous_scale="Blues"
)

st.plotly_chart(fig_kda, width="stretch")



st.subheader("Distribucion de duracion de partidas")

fig_duration = px.histogram(
    df,
    x="duration_minutes",
    nbins=20,
    title="Distribucion de duracion de partidas",
    labels={"duration_minutes": "Duracion (minutos)", "count": "Cantidad de partidas"},
    color_discrete_sequence=["#1f77b4"]
)

st.plotly_chart(fig_duration, use_container_width=True)