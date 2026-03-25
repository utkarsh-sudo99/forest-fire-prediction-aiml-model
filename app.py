import streamlit as st
import base64

def set_background(image_file):
    with open(image_file, "rb") as file:
        encoded = base64.b64encode(file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{encoded}"); 
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_background("forest.jpg")

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import plotly.express as px

st.sidebar.title("📘 Project Info")
st.sidebar.markdown("""
**Forest Fire Prediction App**  
This fire prediction system leverages machine learning to assess environmental conditions 
and forecast fire risk with precision. By analyzing variables like temperature, humidity, 
wind speed, and rainfall, the model identifies high-risk zones and visualizes them through 
interactive charts and heatmaps. The monthly animation reveals seasonal patterns in fire behavior, 
while the feature importance analysis highlights which factors contribute most to ignition. 
Designed for clarity and impact, the app combines technical accuracy with clean visual storytelling—making 
it a powerful tool for both academic evaluation and real-world awareness.
""")

df = pd.read_csv('C:\\Users\\Utkarsh Singh\\Downloads\\New folder\\forest.csv')
df['month'] = df['month'].astype('category').cat.codes
df['day'] = df['day'].astype('category').cat.codes
X = df[['temp', 'RH', 'wind', 'rain']]
y = (df['area'] > 0).astype(int)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

st.title("🔥 Forest Fire Prediction App")
st.write("Enter environmental conditions to predict fire risk:")

temp = st.slider("Temperature (°C)", 0, 50, 20)
rh = st.slider("Relative Humidity (%)", 0, 100, 40)
wind = st.slider("Wind Speed (km/h)", 0, 50, 10)
rain = st.slider("Rainfall (mm)", 0, 20, 0)

if st.button("Predict Fire Risk"):
    input_data = pd.DataFrame([[temp, rh, wind, rain]], columns=['temp', 'RH', 'wind', 'rain'])
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]  

    if prediction == 1:
        st.error(f"⚠️ High Fire Risk! (Confidence: {probability:.2f})")
    else:
        st.success(f"✅ Low Fire Risk (Confidence: {1 - probability:.2f})")

    result = pd.DataFrame({
        "Temperature": [temp],
        "Humidity": [rh],
        "Wind": [wind],
        "Rain": [rain],
        "Fire Risk": ["High" if prediction == 1 else "Low"],
        "Confidence": [f"{probability:.2f}"]
    })
    st.download_button("Download Prediction", result.to_csv(index=False), "prediction.csv", "text/csv")     

df['fire_risk'] = model.predict(df[['temp', 'RH', 'wind', 'rain']])
print(df.columns)

fig = px.scatter(
    df,
    x='temp',
    y='RH',
    animation_frame='month',
    color='fire_risk',
    size='area',
    hover_data=['wind', 'rain'],
    title='🔥 Monthly Fire Risk Animation',
    labels={'temp': 'Temperature (°C)', 'RH': 'Humidity (%)', 'fire_risk': 'Fire Risk'}
)

st.plotly_chart(fig, use_container_width=True)

df['fire_risk'] = model.predict(df[['temp', 'RH', 'wind', 'rain']])

heatmap_data = df.pivot_table(index='RH', columns='temp', values='fire_risk', aggfunc='mean')

fig = px.imshow(
    heatmap_data,
    labels=dict(x="Temperature (°C)", y="Humidity (%)", color="Avg Fire Risk"),
    color_continuous_scale='hot',
    title="🔥 Fire Risk Heatmap (Temp vs Humidity)"
)

fig.update_layout(
    autosize=False,
    width=1000,  
    height=600,
    margin=dict(l=50, r=50, t=80, b=80),  
    xaxis=dict(tickangle=0, title_font=dict(size=16)),
    yaxis=dict(title_font=dict(size=16)),
    font=dict(size=14)
)

st.plotly_chart(fig, use_container_width=False)