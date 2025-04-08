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

# importa funções relacionadas a limpeza de dados, que são utilizadas em todas as páginas
from utils import clean_data


# -------------------------------
# Funções específicas desta página
# -------------------------------
def draw_map():
    '''
    Esta função indica a localização dos restaurantes no mapa mundi, além de agrupar os restaurantes por proximidade
    '''
    map_ = folium.Map( zoom_start=14 )
    marker_cluster = MarkerCluster().add_to(map_)
    for index, location_info in df2.iterrows():

        restaurant_name = location_info['restaurant_name']
        preco_para_dois = location_info['average_cost_for_two']
        moeda = location_info['currency']
        culinaria = location_info['cuisines']
        avaliacao = location_info['aggregate_rating']
        cor = location_info['color_name']


        html = f"<p><strong>{restaurant_name}</strong></p>"
        html += f"<p>Price: {preco_para_dois},00 ({moeda}) para dois"
        html += f"<br />Type: {culinaria}"
        html += f"<br />Aggragate Rating: {avaliacao}/5.0"
   
        popup = folium.Popup(
            folium.Html(html, script=True),
            max_width=600,
        )
        
    
        folium.Marker( [location_info['latitude'],
        location_info['longitude']], icon=folium.Icon(color=cor),
        popup=popup ).add_to(marker_cluster)    

    folium_static(map_, width=1024, height=600 )

    
    


# ---------------- Início da Estrutura lógica do código --------

st.set_page_config( page_title='Home', page_icon='📊', layout='wide')


# Import dataset
df = pd.read_csv("dataset/zomato.csv")

# Limpando os dados
df1 = clean_data(df)


st.markdown('# Fome Zero!')
st.markdown('## O Melhor lugar para encontrar seu mais novo restaurante favorito!')
st.markdown('### Temos as seguintes marcas dentro da nossa plataforma:')


#############################
#Barra Lateral
##############################

scol1, scol2 = st.sidebar.columns([1, 5])
image = Image.open('logo.png')
scol1.image( image)

scol2.markdown('# Fome Zero')

st.sidebar.markdown('# Filtros')
#st.sidebar.markdown('### Escolha os Paises que Deseja visualizar as Informações')

country_options = st.sidebar.multiselect(
    'Escolha os Paises que Deseja visualizar as informações no Mapa',
    ['Philippines', 'Brazil', 'Australia', 'United States of America',
       'Canada', 'Singapure', 'United Arab Emirates', 'India',
       'Indonesia', 'New Zeland', 'England', 'Qatar', 'South Africa',
       'Sri Lanka', 'Turkey'],    
    default=['Brazil', 'England', 'Qatar', 'South Africa', 'Canada', 'Australia'] )


# Filtro de país
linhas_selecionadas = df1['country_name'].isin(country_options)
df2 = df1.loc[linhas_selecionadas, :]



##############################
#layout no streamlit
##############################

with st.container():
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        total_rest = df1['restaurant_id'].nunique()
        col1.metric('Restaurantes Cadastrados', total_rest)
    
    with col2:
        total_pais = df1['country_name'].nunique()
        col2.metric('Países Cadastrados', total_pais)
        
    with col3:
        total_city = df1['city'].nunique()
        col3.metric('Cidades Cadastradas', total_city)

    with col4:
        total_avaliacoes = df1['votes'].sum()
        total_avaliacoes = f"{df1['votes'].sum():,}".replace(",", ".")
        col4.metric('Avaliações Feitas na Plataforma', total_avaliacoes)

    with col5:
        total_cuisines = df1['cuisines'].nunique()
        col5.metric('Tipos de Culinárias Oferecidas', total_cuisines)


with st.container():
    draw_map()






