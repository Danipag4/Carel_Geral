import streamlit as st 
import pandas as pd 
import plotly_express as px 
#import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

#color = st.color_picker("Pick A Color", "#00f900")
#st.write("The current color is", color)

df = pd.read_csv("Aval_Carel.csv", sep=",")


df=df.sort_values("Nivel avaliação")

df["Colab"] = df["Nome"]
df["Compet"] = df["Competencia"]
df["Setor"] = df["Nivel avaliação"]
df["Setorial"] = df["Nivel avaliação"]

st.write("""
# Carel - Análise de Competências
""" )
aval = ["Autoavaliação","Gestor","Pares","Liderados"]

#st.sidebar.write("""
#### Avaliador
#""" )

#st.sidebar.write("""
### Paulo Signorini
#""" )

Nome = st.selectbox("Setor",df["Setor"].unique())

df_filtered = df[df["Setor"] == Nome]
#df_filtered
df_Média = df_filtered.groupby("Compet")[["Autoavaliação","Gestor","Pares","Liderados"]].mean().round(decimals=2).reset_index()
#df_Média

aval = ["Autoavaliação","Gestor","Pares","Liderados"]
#----------------------------------------------------------------------

st.write("""
## Setor
""" ), Nome

fig_comp = px.bar(df_Média, y=aval, x="Compet", barmode='group', color_discrete_map = {"Autoavaliação":"Red", "Gestor":"Blue","Pares":"Yellow", "Liderados":"MediumPurple"})
fig_comp.update_layout(xaxis_title="Competências", yaxis_title="Médias")

fig_comp

#df_filtered

#-------------------------------------------------------------------------------------------

#st.write("""
### Análise das Perguntas
#""" ), Nome

#df_CompetUniq = df_filtered["Competencia"].dropna().reset_index(drop = True)

#unica_Competencia = st.selectbox("Escolha a Competência",df_CompetUniq.unique(),index=1)

#$df_filtered2 = df_filtered[df["Compet"] == unica_Competencia]

#fig_Perg = px.bar(df_filtered2, y="Pergunta", x=aval, orientation="h", barmode='group', color_discrete_map = {"Autoavaliação":"Red", "Gestor":"Blue","Pares":"Yellow", "Liderados":"MediumPurple"})
#fig_Perg.update_layout(xaxis_title="Médias", yaxis_title="Perguntas")
#fig_Perg

#coment = st.checkbox("Comentários")
##df_filtered2
#df_Comenta=df_filtered2["Comentários"].dropna().reset_index(drop = True)
##df_Comenta
#if coment:
#    df_Comenta

#-----------------------------------------------------------------------------------------

st.write("""
## Desempenho Geral por Colaborador
""" ), Nome
#col1, col2 = st.columns(2)

#with col1:
#Compet_Setor = st.selectbox("Defina o Setor",df["Nivel avaliação"].unique(),index=1)
#df_filtered4 = df[df["Setor"] == Compet_Setor]
#df_Comp = df_filtered4["Compet"].dropna().reset_index(drop = True)

#with col2:
aval2 = ["Autoavaliação","Gestor"]
Compet_Desemp = Nome
#Compet_Desemp = st.selectbox("Defina o Setor",df["Setor"].unique(),index=1)
df_filtered5 = df[df["Setor"] == Compet_Desemp]

df_MédiaGeral = df_filtered5.groupby("Nome")[["Autoavaliação","Gestor"]].mean().round(decimals=2).reset_index()
#df_MédiaGeral

fig_DesenvGeral = px.bar(df_MédiaGeral, x=aval2, y="Nome", orientation="h", barmode='group',color_discrete_map = {"Autoavaliação":"Red", "Gestor":"Blue","Pares":"Yellow", "Liderados":"MediumPurple"})
fig_DesenvGeral.update_layout(xaxis_title="Média", yaxis_title="Colaborador")
fig_DesenvGeral



