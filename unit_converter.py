import streamlit as st

# Function to convert temperature separately
def convert_temperature(value, unit_from, unit_to):
    conversions = {
        ("Celsius", "Fahrenheit"): lambda x: (x * 9/5) + 32,
        ("Fahrenheit", "Celsius"): lambda x: (x - 32) * 5/9,
        ("Celsius", "Kelvin"): lambda x: x + 273.15,
        ("Kelvin", "Celsius"): lambda x: x - 273.15,
        ("Fahrenheit", "Kelvin"): lambda x: (x - 32) * 5/9 + 273.15,
        ("Kelvin", "Fahrenheit"): lambda x: (x - 273.15) * 9/5 + 32,
    }
    return conversions.get((unit_from, unit_to), lambda x: "Invalid conversion")(value)

# Function to convert other units
def convert_units(value, unit_from, unit_to):
    conversions = {
        "meters": {"kilometers": 0.001, "centimeters": 100, "millimeters": 1000, "miles": 0.000621371, "yards": 1.09361, "feet": 3.28084, "inches": 39.3701},
        "grams": {"kilograms": 0.001, "milligrams": 1000, "pounds": 0.00220462, "ounces": 0.035274},
        "liters": {"milliliters": 1000, "cubic meters": 0.001, "gallons": 0.264172, "cups": 4.22675},
        "pascals": {"atm": 0.0000098692, "bar": 0.00001, "torr": 0.00750062},
    }
    
    if unit_from in conversions and unit_to in conversions[unit_from]:
        return value * conversions[unit_from][unit_to]
    elif unit_to in conversions and unit_from in conversions[unit_to]:
        return value / conversions[unit_to][unit_from]
    else:
        return "Conversion not supported"

# Streamlit UI setup
st.title("🌍 Professional Unit Converter 🧮 by Hafiza Alina Yasmeen")
st.write("Convert various types of units including length, weight, temperature, pressure, and volume.")

# Unit categories
type_of_conversion = st.selectbox("Select Category", ["Length", "Weight", "Temperature", "Pressure", "Volume"])

# Define unit options based on category
unit_options = {
    "Length": ["meters", "kilometers", "centimeters", "millimeters", "miles", "yards", "feet", "inches"],
    "Weight": ["grams", "kilograms", "milligrams", "pounds", "ounces"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "Pressure": ["pascals", "atm", "bar", "torr"],
    "Volume": ["liters", "milliliters", "cubic meters", "gallons", "cups"]
}

unit_from = st.selectbox("Convert from:", unit_options[type_of_conversion])
unit_to = st.selectbox("Convert to:", unit_options[type_of_conversion])
value = st.number_input("Enter value:", min_value=0.0, step=0.1)

# Button to trigger conversion
if st.button("Convert"):
    if type_of_conversion == "Temperature":
        result = convert_temperature(value, unit_from, unit_to)
    else:
        result = convert_units(value, unit_from, unit_to)
    st.success(f"Converted Value: {result}")