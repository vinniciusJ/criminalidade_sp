import streamlit as st
import pandas as pd
import pydeck as pdk

# carregra os dados

df = pd.read_csv('data/criminalidade_sp_2.csv')

# dashboard

st.title('Criminalidade em São Paulo')
st.markdown(
    """
    A __Criminalidade__ é um problema recorrente no Brasil.
    Buscamos sempre formas de diminuir esses índices e usando técnicas de Ciências de Dados 
    conseguimos entender melhor o que estpa acontecendo e gerar insights
    que direcionem ações capazes de diminuir os índices de criminalidade.
    """
)
#side bar

st.sidebar.info('Foram carregradas {} linhas'.format(df.shape[0]))

if st.sidebar.checkbox('Ver tabela com dados'):
    st.header('Raw Data')
    st.write(df)

df.time = pd.to_datetime(df.time)
ano_selecionado = st.sidebar.slider('Selecione um ano:', 2010, 2018, 2015)
df_selected = df[df.time.dt.year == ano_selecionado]

st.map(df_selected)

st.pydeck_chart(
    pdk.Deck(
        initial_view_state = pdk.ViewState(
            latitude= 23.5505,
            longitude= 46.6333,
            zoom=8,
            pitch=50
        ),
        layers = [
            pdk.Layer(
                'HexagonLayer',
                data = df_selected[['latitude', 'longitude']],
                get_position = '[longitude, latitude]',
                auto_highlight = True,
                elevation_scale = 50,
                pickable = True,
                elevation_range = [0, 3000],
                extruded = True,
                coverage = 1
            )
        ]
    )
)