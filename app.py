import streamlit as st
import joblib # Serialization
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

ed = pd.read_csv("covid_india.csv")
#df = df.rename(columns={'Date':'date','State/UnionTerritory':'state'})
#df = df.rename(columns={'Cured':'Cured','Deaths':'death','Confirmed':'confirm'})
#df = df['Active_Cases']=df['Confirmed']-(df['Cured']+df['Deaths'])
ed = ed[{'Date','State/UnionTerritory','Cured','Deaths','Confirmed'}]
ed = ed[ed['Date']=='2021-08-11']

ed = ed.sort_values(by='Confirmed', ascending=False)
ed = ed.head(5)

df = ed.groupby('State/UnionTerritory')['Confirmed','Deaths','Cured'].max().reset_index()

st.title("Covid-19 Dashboard For India")
st.markdown('The dashboard will visualize the Covid-19 Situation in India')
#st.markdown('Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered coronavirus. Most people infected with the COVID-19 virus will experience mild to moderate respiratory illness and recover without requiring special treatment.')
st.sidebar.title("Visualization Selector")
st.sidebar.markdown("Select the Charts/Plots accordingly:")

select = st.sidebar.selectbox('Visualization type', ['Bar plot', 'Pie chart'], key='1')
if not st.sidebar.checkbox("Hide", False, key='1'):
    if select == 'Pie chart':
                        st.title("Selected top 5 States")
                        fig1 = px.pie(df, values=df["Confirmed"][:5], names=df["State/UnionTerritory"][:5], title="Total Confirmed Cases")
                        st.plotly_chart(fig1)

    if select=='Bar plot':
                        st.title("Selected Top 5 States")
                        fig2 = go.Figure(data=[
                        go.Bar(name='Confirmed', x=df['State/UnionTerritory'][:5], y=df['Confirmed'][:5]),
                        go.Bar(name='Cured', x=df['State/UnionTerritory'][:5], y=df['Cured'][:5]),
                        go.Bar(name='Deaths', x=df['State/UnionTerritory'][:5], y=df['Deaths'][:5])])
                        st.plotly_chart(fig2)

df2 = pd.read_csv('covid_india.csv')
df2['Date'] =  df2['Date'].astype('datetime64[ns]')
select1 = st.sidebar.selectbox('Select', ['Confirmed', 'Cured'], key='2')
if not st.sidebar.checkbox("Hide", False, key='3'):
    if select1 == 'Confirmed':
        fig3 = px.line(df2, x="Date", y="Confirmed")
        st.plotly_chart(fig3)
    elif select1 == 'Cured':
        fig6 = px.line(df2, x="Date", y="Cured")
        st.plotly_chart(fig6)

select2 = st.sidebar.selectbox('Select', ['Confirmed', 'Cured'], key='3')
if not st.sidebar.checkbox("Hide", False, key='4'):
    if select2 == 'Confirmed':
        fig4 = px.area(df2, x="Date", y="Confirmed")
        st.plotly_chart(fig4)
    elif select1 == 'Cured':
        fig5 = px.area(df2, x="Date", y="Cured")
        st.plotly_chart(fig5)
        
left_column, right_column = st.columns(2)
left_column.plotly_chart(fig1, use_container_width=True)
right_column.plotly_chart(fig3, use_container_width=True)

