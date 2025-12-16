import streamlit as st
import pandas as pd
import pickle
import numpy as np

@st.cache_resource
def load_model():
    with open('model_C=1.0.bin', 'rb') as f_in:
        dv, model = pickle.load(f_in)
    return dv, model

@st.cache_data
def load_data():
    df = pd.read_csv('used_cars.csv')

    df.columns = df.columns.str.lower().str.replace(' ', '_')
    string_columns = list(df.dtypes[df.dtypes == 'object'].index)
    for col in string_columns:
        df[col] = df[col].str.lower().str.replace(' ', '_')
    
    return df

dv, model = load_model()
df = load_data()


st.title("Car Price Predictor Pro")
st.write("Choose parameters of car to find out its price")

st.sidebar.header("Car parameters")

makes = sorted(df['make'].unique())
selected_make = st.sidebar.selectbox('Make', makes)

filtered_models = sorted(df[df['make'] == selected_make]['model'].unique())
selected_model = st.sidebar.selectbox('Model', filtered_models)

transmission = st.sidebar.selectbox("Transmission type", sorted(df['transmission_type'].unique()))
drive_wheels = st.sidebar.selectbox("Driven wheels", sorted(df['driven_wheels'].unique()))
vehicle_size = st.sidebar.selectbox("Vehicle size", sorted(df['vehicle_size'].unique()))
vehicle_style = st.sidebar.selectbox("Vehicle style", sorted(df['vehicle_style'].unique()))

year = st.sidebar.number_input("Year of production", min_value=1990, max_value=2024, value=2015, step=1)
engine_hp = st.sidebar.number_input("Power", min_value=50, max_value=1000, value=300, step=10)

cylinders_list = sorted(df['engine_cylinders'].dropna().unique())
engine_cylinders = st.sidebar.selectbox("Number of cylinders", cylinders_list)

highway_mpg = st.sidebar.slider("Highway (MPG)", min_value=10, max_value=100, value=25)
city_mpg = st.sidebar.slider("City (MPG)", min_value=5, max_value=80, value=18)
popularity = st.sidebar.slider("Popularity index", 0, 5000, 1000)

input_data = {
    'make': selected_make,
    'model': selected_model,
    'year': year,
    'engine_hp': engine_hp,
    'engine_cylinders': engine_cylinders,
    'transmission_type': transmission,
    'driven_wheels': drive_wheels,
    'number_of_doors': 4, # default
    'market_category': 'luxury', # default
    'vehicle_size': vehicle_size,
    'vehicle_style': vehicle_style,
    'highway_mpg': highway_mpg,
    'city_mpg': city_mpg,
    'popularity': popularity
}

if st.button("Evaluate price"):
    X=dv.transform([input_data])
    price = np.expm1(model.predict(X)[0])

    st.subheader(f"Result:")
    st.success(f"The estimated price: ${price:,.2f}")

    st.caption(f"Car: {selected_make.upper()} {selected_model.upper()}, {year} year.")