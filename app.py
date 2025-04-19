import streamlit as st

# Title
st.title("🌟 Google Style Unit Converter")

# Sidebar for categories
category = st.sidebar.selectbox("Choose a category:", 
                                ["Length", "Weight", "Temperature", "Time"])

# Define conversion functions
def length_converter(value, from_unit, to_unit):
    units = {
        "meter": 1,
        "kilometer": 1000,
        "mile": 1609.34,
        "centimeter": 0.01,
        "millimeter": 0.001
    }
    return value * units[from_unit] / units[to_unit]

def weight_converter(value, from_unit, to_unit):
    units = {
        "gram": 1,
        "kilogram": 1000,
        "pound": 453.592
    }
    return value * units[from_unit] / units[to_unit]

def temperature_converter(value, from_unit, to_unit):
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return value * 9/5 + 32
        elif to_unit == "Kelvin":
            return value + 273.15
    if from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
    if from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
    return value

def time_converter(value, from_unit, to_unit):
    units = {
        "second": 1,
        "minute": 60,
        "hour": 3600
    }
    return value * units[from_unit] / units[to_unit]

# Select units based on category
if category == "Length":
    units = ["meter", "kilometer", "mile", "centimeter", "millimeter"]
    converter = length_converter
elif category == "Weight":
    units = ["gram", "kilogram", "pound"]
    converter = weight_converter
elif category == "Temperature":
    units = ["Celsius", "Fahrenheit", "Kelvin"]
    converter = temperature_converter
elif category == "Time":
    units = ["second", "minute", "hour"]
    converter = time_converter

# Input fields
from_unit = st.selectbox("From:", units)
to_unit = st.selectbox("To:", units)
value = st.number_input("Enter value:", min_value=0.0)

# Convert button
if st.button("Convert"):
    result = converter(value, from_unit, to_unit)
    st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

