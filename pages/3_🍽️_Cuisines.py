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
# Funções
# -------------------------------

def top_culinarias(df1, ascending):
    ''' Cria um gráfico com os tipos de culinárias que possuem os melhores ou piores tipo de culinária.

        Parâmetros:
            df1: dataframe
            ascending: True ou False
                Determina a classificação das culinárias será ascendente ou descendente
 
        Retorno: Gráfico
        
    '''
    df_aux = df1.loc[df1['rating_text'] != 'Not rated']
    df_aux = (df_aux.loc[:,['aggregate_rating','cuisines']].groupby(['cuisines'])
                                        .mean()
                                        .sort_values(by=['aggregate_rating'], ascending=ascending)
                                        .reset_index() )
    df_aux = df_aux.loc[0:qtde_rest-1,:]

    if (ascending == True):
        classif = "Piores"
    else:
        classif = "Melhores"

    fig = px.bar(df_aux, x="cuisines", y="aggregate_rating", text_auto=".2f",
                 labels={
                     "cuisines":"Tipo de Culinária",
                     "aggregate_rating":"Média da avaliação Média"},
                 title=f"Top {qtde_rest} {classif} Tipos de Culinárias")
    return fig




# ---------------- Início da Estrutura lógica do código --------

# Import dataset
df = pd.read_csv("dataset/zomato.csv")

# Limpando os dados
df1 = clean_data(df)



st.set_page_config( page_title='Cuisines', page_icon='🍽️', layout='wide')

st.title('🍽️ Visão Tipo de Culinárias')
st.markdown('## Melhores Restaurantes dos Principais tipos Culinários')


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


qtde_rest = st.sidebar.slider(
    'Selecione a quantidade de Restaurantes que deseja visualizar',
    value=10,
    min_value=1,
    max_value=20 )


cuisines_options = st.sidebar.multiselect(
    'Escolha os tipos de culinária',
    ['Italian', 'European', 'Filipino', 'American', 'Korean', 'Pizza',
       'Taiwanese', 'Japanese', 'Coffee', 'Chinese', 'Seafood',
       'Singaporean', 'Vietnamese', 'Latin American', 'Healthy Food',
       'Cafe', 'Fast Food', 'Brazilian', 'Argentine', 'Arabian', 'Bakery',
       'Tex-Mex', 'Bar Food', 'International', 'French', 'Steak',
       'German', 'Sushi', 'Grill', 'Peruvian', 'North Eastern',
       'Ice Cream', 'Burger', 'Mexican', 'Vegetarian', 'Contemporary',
       'Desserts', 'Juices', 'Beverages', 'Spanish', 'Thai', 'Indian',
       'Mineira', 'BBQ', 'Mongolian', 'Portuguese', 'Greek', 'Asian',
       'Author', 'Gourmet Fast Food', 'Lebanese', 'Modern Australian',
       'African', 'Coffee and Tea', 'Australian', 'Middle Eastern',
       'Malaysian', 'Tapas', 'New American', 'Pub Food', 'Southern',
       'Diner', 'Donuts', 'Southwestern', 'Sandwich', 'Irish',
       'Mediterranean', 'Cafe Food', 'Korean BBQ', 'Fusion', 'Canadian',
       'Breakfast', 'Cajun', 'New Mexican', 'Belgian', 'Cuban', 'Taco',
       'Caribbean', 'Polish', 'Deli', 'British', 'California', 'Others',
       'Eastern European', 'Creole', 'Ramen', 'Ukrainian', 'Hawaiian',
       'Patisserie', 'Yum Cha', 'Pacific Northwest', 'Tea', 'Moroccan',
       'Burmese', 'Dim Sum', 'Crepes', 'Fish and Chips', 'Russian',
       'Continental', 'South Indian', 'North Indian', 'Salad',
       'Finger Food', 'Mandi', 'Turkish', 'Kerala', 'Pakistani',
       'Biryani', 'Street Food', 'Nepalese', 'Goan', 'Iranian', 'Mughlai',
       'Rajasthani', 'Mithai', 'Maharashtrian', 'Gujarati', 'Rolls',
       'Momos', 'Parsi', 'Modern Indian', 'Andhra', 'Tibetan', 'Kebab',
       'Chettinad', 'Bengali', 'Assamese', 'Naga', 'Hyderabadi', 'Awadhi',
       'Afghan', 'Lucknowi', 'Charcoal Chicken', 'Mangalorean',
       'Egyptian', 'Malwani', 'Armenian', 'Roast Chicken', 'Indonesian',
       'Western', 'Dimsum', 'Sunda', 'Kiwi', 'Asian Fusion', 'Pan Asian',
       'Balti', 'Scottish', 'Cantonese', 'Sri Lankan', 'Khaleeji',
       'South African', 'Drinks Only', 'Durban', 'World Cuisine',
       'Izgara', 'Home-made', 'Giblets', 'Fresh Fish', 'Restaurant Cafe',
       'Kumpir', 'Döner', 'Turkish Pizza', 'Ottoman', 'Old Turkish Bars',
       'Kokoreç'],    
    default=['Home-made', 'BBQ', 'Japanese', 'Brazilian', 'Arabian', 'American', 'Italian'] )




# Filtro de país
linhas_selecionadas = df1['country_name'].isin(country_options)
df2 = df1.loc[linhas_selecionadas, :]

# Filtro de culinária
linhas_selecionadas = df2['cuisines'].isin(cuisines_options)
df3 = df2.loc[linhas_selecionadas, :]


##############################
#layout no streamlit
##############################

with st.container():
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        df_aux = df1.loc[(df1['cuisines']=='Italian')]
        df_aux = df_aux.sort_values(by=['aggregate_rating','restaurant_id'], ascending=[False,True]).reset_index()
        col1.metric(f'Italiana: {df_aux.loc[0,"restaurant_name"]}', f'{df_aux.loc[0,"aggregate_rating"]}/5.0',
                    help = f"""
                    País: {df_aux.loc[0,'country_name']}\n
                    Cidade: {df_aux.loc[0,'city']}\n
                    Média Prato para dois: {df_aux.loc[0,'average_cost_for_two']} ({df_aux.loc[0,'currency']})
                    """)

    with col2:
        df_aux = df1.loc[(df1['cuisines']=='American')]
        df_aux = df_aux.sort_values(by=['aggregate_rating','restaurant_id'], ascending=[False,True]).reset_index()
        col2.metric(f'Americana: {df_aux.loc[0,"restaurant_name"]}', f'{df_aux.loc[0,"aggregate_rating"]}/5.0',
                    help = f"""
                    País: {df_aux.loc[0,'country_name']}\n
                    Cidade: {df_aux.loc[0,'city']}\n
                    Média Prato para dois: {df_aux.loc[0,'average_cost_for_two']} ({df_aux.loc[0,'currency']})
                    """)

    with col3:
        df_aux = df1.loc[(df1['cuisines']=='Arabian')]
        df_aux = df_aux.sort_values(by=['aggregate_rating','restaurant_id'], ascending=[False,True]).reset_index()
        col3.metric(f'Árabe: {df_aux.loc[0,"restaurant_name"]}', f'{df_aux.loc[0,"aggregate_rating"]}/5.0',
                    help = f"""
                    País: {df_aux.loc[0,'country_name']}\n
                    Cidade: {df_aux.loc[0,'city']}\n
                    Média Prato para dois: {df_aux.loc[0,'average_cost_for_two']} ({df_aux.loc[0,'currency']})
                    """)

    with col4:
        df_aux = df1.loc[(df1['cuisines']=='Japanese')]
        df_aux = df_aux.sort_values(by=['aggregate_rating','restaurant_id'], ascending=[False,True]).reset_index()
        col4.metric(f'Japonesa: {df_aux.loc[0,"restaurant_name"]}', f'{df_aux.loc[0,"aggregate_rating"]}/5.0',
                    help = f"""
                    País: {df_aux.loc[0,'country_name']}\n
                    Cidade: {df_aux.loc[0,'city']}\n
                    Média Prato para dois: {df_aux.loc[0,'average_cost_for_two']} ({df_aux.loc[0,'currency']})
                    """)

    with col5:
        df_aux = df1.loc[(df1['cuisines']=='Brazilian')]
        df_aux = df_aux.sort_values(by=['aggregate_rating','restaurant_id'], ascending=[False,True]).reset_index()
        col5.metric(f'Brasileira: {df_aux.loc[0,"restaurant_name"]}', f'{df_aux.loc[0,"aggregate_rating"]}/5.0',
                    help = f"""
                    País: {df_aux.loc[0,'country_name']}\n
                    Cidade: {df_aux.loc[0,'city']}\n
                    Média Prato para dois: {df_aux.loc[0,'average_cost_for_two']} ({df_aux.loc[0,'currency']})
                    """)

    
with st.container():
    st.markdown(f'## Top {qtde_rest} Restaurantes')  
    
    df_aux = df3.sort_values(by=['aggregate_rating','restaurant_id'], ascending=[False,True]).reset_index()
    cols=['restaurant_id', 'restaurant_name', 'country_name', 'city', 'cuisines', 'average_cost_for_two', 'aggregate_rating', 'votes']
    df_aux = df_aux.loc[0:qtde_rest-1,cols]
    
    st.dataframe(df_aux, hide_index=True)
    

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        fig = top_culinarias(df1,False)
        st.plotly_chart(fig, use_container_width=True)
            
    with col2:
        fig = top_culinarias(df1,True)
        st.plotly_chart(fig, use_container_width=True)











