import streamlit as st
import pickle
import pandas as pd

st.write("# Ames Iowa House Price Prediction")

st.write("## Please enter your house details:")

lotarea_input = st.number_input(
    label='Enter lot area, in sqft',
    min_value = 1300,
    max_value = 39000
)

firstfloor_input = st.number_input(
    label='Enter first floor area, in sqft',
    min_value = 350,
    max_value = 2220
)

grlivarea_input = st.number_input(
    label='Enter ground living area area, in sqft',
    min_value = 440,
    max_value = 2975
)

loaded_model = pickle.load(open('models/ames-model.sav', 'rb'))

if st.button('Generate Predictions'):

    test_data = pd.DataFrame(columns = ['LotArea', '1stFlrSF', 'GrLivArea'])

    test_data = test_data.append(
        {
            'LotArea': lotarea_input, 
            '1stFlrSF' : firstfloor_input, 
            'GrLivArea': grlivarea_input
        },
        ignore_index=True)

    prediction = loaded_model.predict(test_data)[0]

    st.write(f"Your predicted house value is: ${prediction:,.2f}")