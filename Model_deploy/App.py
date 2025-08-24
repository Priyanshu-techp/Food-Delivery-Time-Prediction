import pandas as pd
import streamlit as st
import joblib

df = pd.read_csv('Data/Clean_data.csv')
model = joblib.load('Model_deploy/model.pkl')

st.title('Food Delivery Time Prediction')


# Target_col = 'Delivery_Time_min'
#num_col = ['Distance_km', 'Preparation_Time_min', 'Courier_Experience_yrs']
#obj_col = ['Weather', 'Traffic_Level', 'Time_of_Day', 'Vehicle_Type', 'Distance_category']
def Distance(x):
    if x > 0 and x <= 5:
        return 'Very close'
    elif x > 5 and x <= 10:
        return 'Close'
    elif x > 5 and x <= 10:
        return 'Midrange'
    elif x > 10 and x <= 15:
        return 'Far'
    elif x > 15 and x <= 20:
        return 'So far'

with st.sidebar:
    Distance_km = st.slider('Distance_km', 0.0, 20.0, 10.0)
    Preparation_Time_min = st.slider('Preparation_Time_min', 0, 30, 15)
    Courier_Experience_yrs = st.slider('Courier_Experience_yrs', 0, 10, 5)
    Weather = st.selectbox('Weather', df['Weather'].unique())
    Traffic_Level = st.selectbox('Traffic_Level', df['Traffic_Level'].unique())
    Time_of_Day = st.selectbox('Time_of_Day', df['Time_of_Day'].unique())
    Vehicle_Type = st.selectbox('Vehicle_Type', df['Vehicle_Type'].unique())
Distance_category = Distance(Distance_km)

input_dict = {
    "Distance_km" : [Distance_km* 1000],
    "Preparation_Time_min" : [Preparation_Time_min],
    "Courier_Experience_yrs" : [Courier_Experience_yrs],
    "Weather" : [Weather],
    "Traffic_Level" : [Traffic_Level],
    "Time_of_Day" : [Time_of_Day],
    "Vehicle_Type" : [Vehicle_Type],
    "Distance_category" : [Distance_category],
}

input_df = pd.DataFrame(input_dict)

if st.button('Predict Time'):
    st.write(input_df)
    prediction = model.predict(input_df)
    st.success(f"Predicted Delivery Time: {prediction[0]:.2f} minutes")
# Streamlit run 'Model_deploy/App.py'