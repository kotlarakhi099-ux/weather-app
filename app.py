import streamlit as st
import requests

API_KEY = "059c60ea3f8dc32fa5e6846f624d13a0"

st.title("Weather App")

city = st.text_input("Enter city name:")

if st.button("Get Weather"):
    if not city.strip():
        st.warning("Please enter a city name")
    else:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            st.success(f"Weather in {city.capitalize()}: {data['weather'][0]['description']}")
            st.metric("Temperature", f"{data['main']['temp']} °C")
        else:
            st.error(data.get("message", "Failed to retrieve weather data."))