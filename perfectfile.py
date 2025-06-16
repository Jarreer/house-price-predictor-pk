import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Title
st.title("🏡 Karachi House Price Predictor 🇵🇰")
st.write("Enter property details below to estimate its price in PKR.")

# 🧾 Sample Karachi-style dataset (can be replaced with real CSV later)
data = {
    'area': [1200, 1500, 1800, 2200, 2500, 3000, 3500, 4000],
    'bedrooms': [2, 3, 3, 4, 4, 5, 5, 6],
    'city': ['DHA', 'Gulshan', 'DHA', 'Nazimabad', 'Gulshan', 'DHA', 'Nazimabad', 'DHA'],
    'type': ['own', 'rent', 'own', 'rent', 'own', 'own', 'rent', 'own'],
    'price': [15000000, 65000, 18000000, 55000, 16000000, 22000000, 60000, 25000000]  # PKR
}
df = pd.DataFrame(data)

# 🔄 Encode 'city' and 'type' (text to numbers)
df['city_encoded'] = df['city'].astype('category').cat.codes
df['type_encoded'] = df['type'].astype('category').cat.codes

# Feature set
X = df[['area', 'bedrooms', 'city_encoded', 'type_encoded']]
y = df['price']

# Train model
model = LinearRegression()
model.fit(X, y)

# --- User Inputs ---
st.subheader("🔍 Enter Property Details")

area = st.number_input("Enter Area (sqft)", value=1500, min_value=500, max_value=10000, step=100)
bedrooms = st.slider("Number of Bedrooms", 1, 10, 3)

city = st.selectbox("Select Area in Karachi", ['DHA', 'Gulshan', 'Nazimabad'])
property_type = st.radio("Property Type", ['own', 'rent'])

# Convert user input to encoded values
city_encoded = pd.Series([city]).astype('category').cat.codes[0]
type_encoded = 0 if property_type == 'own' else 1  # manually map if needed

# Predict Button
if st.button("💰 Predict Price"):
    features = [[area, bedrooms, city_encoded, type_encoded]]
    prediction = model.predict(features)[0]

    if property_type == 'rent':
        st.success(f"🏷️ Estimated Monthly Rent: ₨ {int(prediction):,}")
    else:
        st.success(f"🏷️ Estimated Property Price: ₨ {int(prediction):,}")