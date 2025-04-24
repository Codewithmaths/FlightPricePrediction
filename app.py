import streamlit as st
import pickle
from datetime import datetime

# Load the pre-trained model
model = pickle.load(open('model1.pkl', 'rb'))

# Dictionaries for categorical variables
airline_dict = {'AirAsia': 0, "Indigo": 1, "GO_FIRST": 2, "SpiceJet": 3, "Air_India": 4, "Vistara": 5}
source_dict = {'Delhi': 0, "Hyderabad": 1, "Bangalore": 2, "Mumbai": 3, "Kolkata": 4, "Chennai": 5}
departure_dict = {'Early_Morning': 0, "Morning": 1, "Afternoon": 2, "Evening": 3, "Night": 4, "Late_Night": 5}
stops_dict = {'zero': 0, "one": 1, "two_or_more": 2}
arrival_dict = {'Early_Morning': 0, "Morning": 1, "Afternoon": 2, "Evening": 3, "Night": 4, "Late_Night": 5}
destination_dict = {'Delhi': 0, "Hyderabad": 1, "Mumbai": 2, "Bangalore": 3, "Chennai": 4, "Kolkata": 5}
class_dict = {'Economy': 0, 'Business': 1}

# Streamlit app
st.title("Flight Fare Prediction")

# Input fields for user data
airline = st.selectbox("Airline", list(airline_dict.keys()))
source_city = st.selectbox("Source City", list(source_dict.keys()))
departure_time = st.selectbox("Departure Time", list(departure_dict.keys()))
stops = st.selectbox("Number of Stops", list(stops_dict.keys()))
arrival_time = st.selectbox("Arrival Time", list(arrival_dict.keys()))
destination_city = st.selectbox("Destination City", list(destination_dict.keys()))
travel_class = st.selectbox("Class", list(class_dict.keys()))
departure_date = st.date_input("Departure Date", min_value=datetime.today())

# Predict button
if st.button("Predict Fare"):
    try:
        # Prepare input features for prediction
        airline_val = airline_dict[airline]
        source_city_val = source_dict[source_city]
        departure_time_val = departure_dict[departure_time]
        stops_val = stops_dict[stops]
        arrival_time_val = arrival_dict[arrival_time]
        destination_city_val = destination_dict[destination_city]
        travel_class_val = class_dict[travel_class]
        date_diff = (departure_date - datetime.today().date()).days + 1
        
        features = [airline_val, source_city_val, departure_time_val, stops_val,
                    arrival_time_val, destination_city_val, travel_class_val, date_diff]
        
        # Get prediction
        prediction = model.predict([features])[0]
        st.success(f"Predicted Fare: ₹{round(prediction, 2)}")
    except Exception as e:
        st.error(f"Error: {str(e)}")