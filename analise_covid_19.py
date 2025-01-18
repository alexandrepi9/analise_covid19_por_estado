import pandas as pd
import plotly.express as px 
import streamlit as st 


df = pd.read_csv("https://raw.githubusercontent.com/wcota/covid19br/refs/heads/master/cases-brazil-states.csv")

df = df.rename(columns={'newDeaths': 'Novos óbitos', 'newCases': 'Novos casos', 'death_per_100k_inhabitants': 'Óbitos por 100 mil habitantes', 'totalCases_per_100k_inhabitants': 'Casos por 100 mil habitantes'})

estados = list(df['state'].unique())
state = st.sidebar.selectbox('Escolha o estado', estados)

#state = 'PE'

#column = 'Casos por 100 mil habitantes'
colunas = ['Novos óbitos', 'Novos casos', 'Óbitos por 100 mil habitantes', 'Casos por 100 mil habitantes']
column = st.sidebar.selectbox('Selecione o tipo de informação', colunas)


df = df[df['state'] == state]

fig = px.line(df, x='date', y=column, title=column + ' - ' + state)
fig.update_layout( xaxis_title = "Data", yaxis_title = column.upper(), title = {'x':0.5})

st.title("DADOS COVID - BRASIL")
st.write("Nessa aplicação, o usuário tem a opção de escolher o estado e o tipo de informação para mostrar no gráfico. Utilize o menu lateral para selecionar")

#fig.show()
st.plotly_chart(fig, use_container_width=True)

st.caption("Os dados foram obtidos no site: https://github.com/wcota/covid19br")