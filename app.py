import streamlit as st
import joblib
import numpy as np

model = joblib.load("LinearRegression.pkl")

st.title("🏠 House Price Predictor 🏠")

bedrooms = st.number_input("Bedrooms", min_value=0, value=3, step=1)
bathrooms = st.number_input("Bathrooms", min_value=0.0, value=2.0, step=0.5)
sqft_living = st.number_input("Sqft Living", min_value=0, value=1800)
sqft_lot = st.number_input("Sqft Lot", min_value=0, value=5000)
floors = st.number_input("Floors", min_value=0, value=1)
waterfront = st.selectbox("Waterfront", [0, 1])
view = st.slider("View", 0, 4, 1)
condition = st.slider("Condition", 1, 5, 3)
grade = st.slider("Grade", 1, 10, 7)
yr_built = st.number_input("Year Built", min_value=1800, value=1995)
yr_renovated = st.number_input("Year Renovated", min_value=0, value=0)

if st.button("Predict Price"):
    input_data = np.array([[bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront,
                            view, condition, grade, yr_built, yr_renovated]])
    prediction = model.predict(input_data)[0]
    st.success(f"🏡 Estimated House Price: ₹{int(prediction):,}")
