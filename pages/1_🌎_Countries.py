from haversine import haversine
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import streamlit as st
from PIL import Image
import folium
from streamlit_folium import folium_static
import inflection
import numpy as np

# importa funções relacionadas a limpeza de dados, que são utilizadas em todas as páginas
from utils import clean_data



# -------------------------------
# Funções específcas desta página
# -------------------------------

def restaurantes_por_pais(df1):
    ''' Esta função cria um gráfico com a quantidade de restaurantes registados por país.

        Parâmetros:
            df1: dataframe
        
        Retorno: Gráfico
        
    '''
    df_aux = (df1.loc[:,['restaurant_id','country_name']].groupby('country_name')
                                        .nunique()
                                        .sort_values(by='restaurant_id', ascending=False)
                                        .reset_index() )

    #Gráfico
    fig = px.bar(df_aux, x="country_name", y="restaurant_id", text_auto=True,
                 labels={
                     "country_name":"Paises",
                     "restaurant_id":"Quantidade de Restaurantes"},
                 title="Quantidade de Restaurantes Registrados por País")  

    return fig
        

def cidades_por_pais(df1):
    ''' Esta função cria um gráfico com a quantidade de cidades registadas por país.

        Parâmetros:
            df1: dataframe
        
        Retorno: Gráfico
        
    '''    
    df_aux = (df1.loc[:,['city','country_name']].groupby('country_name')
                                            .nunique()
                                            .sort_values(by='city', ascending=False)
                                            .reset_index() )
   
    #Gráfico
    fig = px.bar(df_aux, x="country_name", y="city", text_auto=True,
                 labels={
                     "country_name":"Paises",
                     "city":"Quantidade de Cidades"},
                 title="Quantidade de Cidades Registradas por País")

    return fig


def avaliacoes_por_pais(df1):
    ''' Esta função cria um gráfico com a quantidade de avaliações registadas por país.

        Parâmetros:
            df1: dataframe
        
        Retorno: Gráfico
        
    '''    
    df_aux = (df1.loc[:,['votes','country_name']].groupby('country_name')
                                            .mean()
                                            .sort_values(by='votes', ascending=False)
                                            .reset_index() )
    df_aux['votes'] = np.round(df_aux['votes'],2)
        
    fig = px.bar(df_aux, x="country_name", y="votes", text_auto=".2f",
                 labels={
                     "country_name":"Paises","votes":"Quantidade de Avaliações"},
                 title="Médias de Avaliações feitas por por País")
    
    return fig



def media_preco_por_pais(df1):
    ''' Esta função cria um gráfico com o preço médio do prato para duas pessoa registado por país.

        Parâmetros:
            df1: dataframe
        
        Retorno: Gráfico
        
    '''    
    df_aux = (df1.loc[:,['average_cost_for_two','country_name']].groupby('country_name')
                                            .mean()
                                            .sort_values(by='average_cost_for_two', ascending=False)
                                            .reset_index() )
        
    
    fig = px.bar(df_aux, x="country_name", y="average_cost_for_two", text_auto=".2f",
                 labels={
                     "country_name":"Paises","average_cost_for_two":"Preço de Prato para duas Pessoas"},
                 title="Média de Preço de um prato para Duas pessoas por País")

    return fig





# ---------------- Início da Estrutura lógica do código --------

st.set_page_config( page_title='Countries', page_icon='🌎', layout='wide')

# Import dataset
df = pd.read_csv("dataset/zomato.csv")

# Limpando os dados
df1 = clean_data(df)



#############################
#Barra Lateral
##############################

st.title('🌎 Visão Países')


st.sidebar.markdown('# Filtros')


country_options = st.sidebar.multiselect(
    'Escolha os Paises que Deseja visualizar as Informações',
    ['Philippines', 'Brazil', 'Australia', 'United States of America',
       'Canada', 'Singapure', 'United Arab Emirates', 'India',
       'Indonesia', 'New Zeland', 'England', 'Qatar', 'South Africa',
       'Sri Lanka', 'Turkey'],    
    default=['Brazil', 'England', 'Qatar', 'South Africa', 'Canada', 'Australia'] )


# Filtro de país
linhas_selecionadas = df1['country_name'].isin(country_options)
df1 = df1.loc[linhas_selecionadas, :]



##############################
#layout no streamlit
##############################

with st.container():
   
    fig = restaurantes_por_pais(df1)
    st.plotly_chart(fig, use_container_width=True)
    

with st.container():

    fig = cidades_por_pais(df1)
    st.plotly_chart(fig, use_container_width=True)
    

with st.container():
    col1, col2 = st.columns(2)
    
    with col1:
        
        fig = avaliacoes_por_pais(df1)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        
        fig = media_preco_por_pais(df1)
        st.plotly_chart(fig, use_container_width=True)












