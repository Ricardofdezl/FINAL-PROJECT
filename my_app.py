import streamlit as st
import pandas as pd

def load_data():
    file_path = 'brands.csv'  
    data = pd.read_csv(file_path)
    return data

st.title("Brandables")
data = load_data()
st.write(f"Total products: {len(data)} items")
st.dataframe(data)

st.sidebar.header("Filter Options")

brands = ["All"] + sorted(data['brand'].unique().tolist())
selected_brand = st.sidebar.selectbox("Select Brand", brands)

sections = ["All"] + sorted(data['section'].unique().tolist())
selected_section = st.sidebar.selectbox("Select Section", sections)

min_price, max_price = data['price'].min(), data['price'].max()
selected_price_range = st.sidebar.slider("Select Price Range", min_price, max_price, (min_price, max_price))

categories = ["All"] + sorted(data['category'].unique().tolist())
selected_category = st.sidebar.selectbox("Select Category", categories)

filtered_data = data

if selected_brand != "All":
    filtered_data = filtered_data[filtered_data['brand'] == selected_brand]

if selected_section != "All":
    filtered_data = filtered_data[filtered_data['section'] == selected_section]

filtered_data = filtered_data[
    (filtered_data['price'] >= selected_price_range[0]) & 
    (filtered_data['price'] <= selected_price_range[1])
]

if selected_category != "All":
    filtered_data = filtered_data[filtered_data['category'] == selected_category]

st.header("Filtered Data")
st.write(f"Filtered results: {len(filtered_data)} items")
st.dataframe(filtered_data)