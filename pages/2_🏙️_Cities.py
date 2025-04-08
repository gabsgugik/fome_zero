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

from utils import clean_data


# -------------------------------
# Funções específicas desta página
# -------------------------------

def cidades_mais_restaurantes(df1):
    ''' Cria um gráfico com as cidades que possuem mais restaurantes.

        Parâmetros:
            df1: dataframe
        
        Retorno: Gráfico
        
    '''
    df_aux = (df1.loc[:,['restaurant_id','city','country_name']].groupby(['city','country_name'])
                                            .nunique()
                                            .sort_values(by=['restaurant_id'], ascending=False)
                                            .reset_index() )
    df_aux = df_aux.loc[0:9,:]

    fig = px.bar(df_aux, x="city", y="restaurant_id", text_auto=True, color="country_name",
                     labels={
                         "city":"Cidades",
                         "country_name":"País",
                         "restaurant_id":"Quantidade de Restaurantes"},
                     title="Top 10 Cidades com mais Restaurantes na Base de Dados")

    return fig


def cidades_restaurantes_media(df1, operacao, valor):
    ''' Esta função cria um gráfico com as cidades que possuem as maiores médias de avaliação acima ou abaixo de determinada nota.

        Parâmetros:
            df1: dataframe
            operacao: "acima" ou "abaixo
                Determina se comparação será feita acima ou abaixo de determinada nota
            valor: float
                Valor da nota a ser comparada
 
        Retorno: Gráfico    
       
    '''
    
    if (operacao == 'acima'):
        df_aux = df1.loc[df1['aggregate_rating']>=valor]   
        strt = f"acima de {valor}"
    else:
        df_aux = df1.loc[df1['aggregate_rating']<valor]   
        strt = f"abaixo de {valor}"

    df_aux = (df_aux.loc[:,['restaurant_id','city','country_name']].groupby(['city','country_name'])
                                        .nunique()
                                        .sort_values(by=['restaurant_id'], ascending=False)
                                        .reset_index() )
    df_aux = df_aux.loc[0:6,:]
    
    fig = px.bar(df_aux, x="city", y="restaurant_id", text_auto=True, color="country_name",
                 labels={
                     "city":"Cidades",
                     "country_name":"País",
                     "restaurant_id":"Quantidade de Restaurantes"},
                 title=f"Top 7 cidades com Restaurantes com média de avaliação {strt}" )                

    return fig


    
def cidades_culinarias_distintas(df1):
    ''' Esta função cria um gráfico com as cidades que possuem mais tipos de culinárias distintos.

        Parâmetros:
            df1: dataframe
        
        Retorno: Gráfico
        
    '''
    df_aux = (df1.loc[:,['cuisines','city','country_name']].groupby(['city','country_name'])
                                            .nunique()
                                            .sort_values(by=['cuisines'], ascending=False)
                                            .reset_index() )
    df_aux = df_aux.loc[0:9,:]

    fig = px.bar(df_aux, x="city", y="cuisines", text_auto=True, color="country_name",
                     labels={
                         "city":"Cidades",
                         "country_name":"País",
                         "cuisines":"Quantidade de Tipos Culinários Únicos"},
                     title="Top 10 cidades com mais restaurantes com tipos culinários distintos")

    return fig
    


# ---------------- Início da Estrutura lógica do código --------

st.set_page_config( page_title='Cities', page_icon='🏙️', layout='wide')

st.title('🏙️ Visão Cidades')


# Import dataset
df = pd.read_csv("dataset/zomato.csv")

# Limpando os dados
df1 = clean_data(df)


#############################
#Barra Lateral
##############################

st.sidebar.markdown('# Filtros')
#st.sidebar.markdown('### Escolha os Paises que Deseja visualizar as Informações')

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

    fig = cidades_mais_restaurantes(df1)
    st.plotly_chart(fig, use_container_width=True)  

 
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        fig = cidades_restaurantes_media(df1, 'acima', 4)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig = cidades_restaurantes_media(df1, 'abaixo', 2.5)
        st.plotly_chart(fig, use_container_width=True)
        


with st.container():
    fig = cidades_culinarias_distintas(df1)
    st.plotly_chart(fig, use_container_width=True)














