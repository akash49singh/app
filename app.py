import streamlit as st # web development
import numpy as np # np mean, np random 
import pandas as pd # read csv, df manipulation
import time # to simulate a real time data, time loop 
import plotly.express as px # interactive charts 


# read csv from a github repo
df = pd.read_csv("covid_india.csv")


st.set_page_config(
    page_title = 'Real-Time Dashboard',
    page_icon = '✅',
    layout = 'wide'
)

# dashboard title

st.title("Real-Time / Live Data Science Dashboard")

# top-level filters 

state_filter = st.selectbox("Select the state", pd.unique(df['State/UnionTerritory']))


# creating a single-element container.
placeholder = st.empty()

# dataframe filter 

df = df[df['State/UnionTerritory']==state_filter]

# near real-time / live feed simulation 

for seconds in range(200):
#while True: 
    
    df['Confirmed'] = df['Confirmed'] * np.random.choice(range(1,5))
    df['Deaths'] = df['Deaths'] * np.random.choice(range(1,5))

    # creating KPIs 
    avg_age = np.count_nonzero(df['Confirmed']) 

    count_married = int(df[(df["Cured"]=='Cured')]['Cured'].count() + np.random.choice(range(1,30)))
    
    balance = np.mean(df['Deaths'])

    with placeholder.container():
        # create three columns
        kpi1, kpi2, kpi3 = st.columns(3)

        # fill in those three columns with respective metrics or KPIs 
        kpi1.metric(label="Age ⏳", value=round(avg_age), delta= round(avg_age) - 10)
        kpi2.metric(label="Married Count 💍", value= int(count_married), delta= - 10 + count_married)
        kpi3.metric(label="A/C Balance ＄", value= f"$ {round(balance,2)} ", delta= - round(balance/count_married) * 100)

        # create two columns for charts 

        fig_col1, fig_col2 = st.columns(2)
        with fig_col1:
            st.markdown("### First Chart")
            fig = px.density_heatmap(data_frame=df, y = 'Confirmed', x = 'State/UnionTerritory')
            st.write(fig)
        with fig_col2:
            st.markdown("### Second Chart")
            fig2 = px.histogram(data_frame = df, x = 'Confirmed')
            st.write(fig2)
        st.markdown("### Detailed Data View")
        st.dataframe(df)
        time.sleep(1)
    #placeholder.empty()


