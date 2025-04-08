from haversine import haversine
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import streamlit as st
from PIL import Image
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static
import inflection
import numpy as np



COUNTRIES = {
    1: "India",
    14: "Australia",
    30: "Brazil",
    37: "Canada",
    94: "Indonesia",
    148: "New Zeland",
    162: "Philippines",
    166: "Qatar",
    184: "Singapure",
    189: "South Africa",
    191: "Sri Lanka",
    208: "Turkey",
    214: "United Arab Emirates",
    215: "England",
    216: "United States of America",
}

def country_name(country_id):
    return COUNTRIES[country_id]


def create_price_tye(price_range):
    if price_range == 1:
        return "cheap"
    elif price_range == 2:
        return "normal"
    elif price_range == 3:
        return "expensive"
    else:
        return "gourmet"

COLORS = {
    "3F7E00": "darkgreen",
    "5BA829": "green",
    "9ACD32": "lightgreen",
    "CDD614": "orange",
    "FFBA00": "red",
    "CBCBC8": "darkred",
    "FF7800": "darkred",
}

def color_name(color_code):
    return COLORS[color_code]


def rename_columns(dataframe):
    ''' Renomea o nome das colunas para um formato mais amigável para o uso em dataframe
        
    '''
    df = dataframe.copy()
    title = lambda x: inflection.titleize(x)
    snakecase = lambda x: inflection.underscore(x)
    spaces = lambda x: x.replace(" ", "")
    cols_old = list(df.columns)
    cols_old = list(map(title, cols_old))
    cols_old = list(map(spaces, cols_old))
    cols_new = list(map(snakecase, cols_old))
    df.columns = cols_new
    return df


def clean_data(df1):
    ''' Esta funcao tem a responsabilidade de limpar o dataframe

        Tipos de limpeza:
        1. Renomeação do nome das colunas
        2. Retiradas de valores NaN
        3. Exclusão de linhas duplicadas
        4. Criação de colunas auxiliares
        5. Separação da coluna "switch_to_order_menu"

        Input: Dataframe
        Output: Dataframe 

    '''

    #  Renomando o nome das colunas
    df1 = rename_columns(df1)

    # Excluindo NaN da coluna cuisines ( 15 ocorrencias)
    df1.dropna(subset=['cuisines'], inplace=True)
    
    # Excuindo linhas duplicadas
    df1.drop_duplicates(inplace=True)
    
    
    df1["cuisines"] = df1.loc[:, "cuisines"].apply(lambda x: x.split(",")[0])
    df1["country_name"] = df1.loc[:, "country_code"].apply(lambda x: country_name(x))
    df1["price_tye"] = df1.loc[:, "price_range"].apply(lambda x: create_price_tye(x))
    df1["color_name"] = df1.loc[:, "rating_color"].apply(lambda x: color_name(x))

    # Coluna switch_to_order_menu possui valor único em todas as linhas
    df1.drop('switch_to_order_menu', axis=1, inplace=True)

    return df1


