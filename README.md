# 🔥 Forest Fire Prediction App

This project is a **Streamlit-based web application** that predicts forest fire risk using machine learning models.  
It combines environmental data analysis with interactive visualizations to raise awareness and support decision-making.

---

## 📖 Project Overview
The app leverages a **Random Forest Classifier** trained on forest fire data to assess fire risk based on:
- 🌡️ Temperature (°C)
- 💧 Relative Humidity (%)
- 🌬️ Wind Speed (km/h)
- 🌧️ Rainfall (mm)

Users can input environmental conditions, receive predictions with confidence scores, and explore interactive charts that reveal seasonal fire patterns and feature importance.

---

## ✨ Features
- **Custom Background**: A visually appealing forest background for immersive experience.
- **Sidebar Info**: Clear project description and context.
- **Interactive Prediction**: Sliders to input conditions and predict fire risk.
- **Downloadable Results**: Export predictions as CSV.
- **Monthly Animation**: Animated scatter plot showing fire risk trends by month.
- **Heatmap Visualization**: Temperature vs. Humidity heatmap highlighting average fire risk.

---

## 🛠️ Tech Stack
- **Frontend**: [Streamlit](https://streamlit.io/) for UI
- **Data Handling**: Pandas
- **Machine Learning**: Scikit-learn (Random Forest Classifier)
- **Visualization**: Plotly Express
- **Utilities**: Base64 for background image encoding

---

## 📂 Dataset
The app uses a dataset (`forest.csv`) containing:
- Temperature, humidity, wind speed, rainfall
- Fire area burned
- Month and day (converted to categorical codes)

---

## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/forest-fire-prediction.git
   cd forest-fire-prediction
