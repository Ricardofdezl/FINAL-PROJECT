import streamlit as st
from FP_Copy1 import load_data  

st.title("Brandables")

data = load_data()
st.dataframe(data)

st.write("Use the filters below to view products by brand, section, price range, and category.")

brands = data['brand'].unique()
selected_brand = st.selectbox("Select a Brand:", options=brands, index=0)

sections = data['section'].unique()
selected_section = st.selectbox("Select a Section:", options=sections, index=0)

categories = data['category'].unique()
selected_category = st.selectbox("Select a Category:", options=categories, index=0)

min_price, max_price = st.slider("Select Price Range:", 
                                 min_value=float(data['price'].min()), 
                                 max_value=float(data['price'].max()), 
                                 value=(float(data['price'].min()), float(data['price'].max())))

filtered_data = data[
    (data['brand'] == selected_brand) &
    (data['section'] == selected_section) &
    (data['category'] == selected_category) &
    (data['price'] >= min_price) &
    (data['price'] <= max_price)
]

st.write(f"Filtered results: {len(filtered_data)} items")
st.dataframe(filtered_data)
