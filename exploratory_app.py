import streamlit as st 
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

st.write("# Exploring Animals")

df = pd.read_csv('data/Austin_Animal_Center_Intakes_061521_with_location_details.csv')

st.sidebar.write("### Example text")

animal_type = st.sidebar.selectbox(
    label='Choose your animal type',
    options=['Dog', 'Cat']
    )
# Input box
st.write(f"## {animal_type} Intake Types")

subset_df = df.loc[df['Animal Type'] == animal_type]

types = subset_df['Intake Type'].value_counts().reset_index()
types = types.rename(columns={'index':'Type', 'Intake Type': 'Count'})

# plotly pie chart
fig = px.pie(types, values='Count', names='Type',
             color_discrete_sequence=px.colors.qualitative.Pastel)
st.write(fig)

if st.button('Say hello'):
    st.write('Why hello there')