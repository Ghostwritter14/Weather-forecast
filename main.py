import streamlit as st
import plotly.express as px
from backend import get_data

# Widgets
st.title("Weather Forecast for the Upcoming Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    # get temp or sky data
    try:
        filtered = get_data(place, days)

        if option == "Temperature":
            temperatures = [dict["main"]["temp"] / 10 for dict in filtered]
            dates = [dict["dt_txt"] for dict in filtered]
            # plot the graph
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature(C)"})
            st.plotly_chart(figure)
        if option == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_state = [dict["weather"][0]["main"] for dict in filtered]
            image_parse = [images[condition] for condition in sky_state]
            st.image(image_parse, width=150)
    except KeyError:
        st.write("The place you entered does not exist")

