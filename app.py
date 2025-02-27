# -*- coding: utf-8 -*-
import streamlit as st
import sys

# Ensure UTF-8 encoding
sys.stdout.reconfigure(encoding="utf-8")

# 🎨 Custom Styling
st.set_page_config(page_title="Unit Converter", page_icon="⚙️", layout="centered")

st.markdown(
    """
    <style>
        body {
            background-color: #0D1117;
            color: white;
        }
        .stApp {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .stButton > button {
            background: linear-gradient(90deg,rgb(40, 98, 205),rgb(12, 83, 237));
            color: white;
            font-weight: bold;
            padding: 10px;
            border-radius: 10px;
            border: none;
        }
        .stButton > button:hover {
            background:rgb(235, 239, 245);
            color:rgb(12, 83, 237);
        }
        .stSelectbox, .stNumber_input {
            background: rgba(255, 255, 255, 0.2);
            color: white;
            border-radius: 10px;
        }

        /* ✅ Blue Color for Title & Sub-Titles */
        h1, h2 {
            color:rgb(12, 83, 237) !important; /* Blue Color */
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# 🌟 Title (Unicode escape for ⚙️ emoji)
st.title("⚙️ Unit Converter")
st.subheader("Convert Units Easily")  # ✅ This will be blue now

# 📌 Sidebar for Navigation
st.sidebar.header("Select Conversion Type")
conversion_type = st.sidebar.selectbox(
    "Choose Conversion", ["Length", "Weight", "Temperature", "Pressure", "Speed", "Time"]
)

# 📏 Conversion Function
def convert_units(value, from_unit, to_unit):
    conversion_factors = {
        "Length": {"meters": 1, "kilometers": 0.001, "miles": 0.000621371},
        "Weight": {"grams": 1, "kilograms": 0.001, "pounds": 0.00220462},
        "Speed": {"meters per second": 1, "kilometers per hour": 3.6, "miles per hour": 2.23694},
        "Pressure": {"pascals": 1, "kilopascals": 0.001, "bar": 0.00001, "psi": 0.000145038}
    }
    
    if conversion_type in conversion_factors:
        return value * (conversion_factors[conversion_type][to_unit] / conversion_factors[conversion_type][from_unit])
    
    elif conversion_type == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9 / 5) + 32
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5 / 9
        else:
            return value

# 🕽️ User Input
value = st.number_input("Enter Value:", min_value=0.0, format="%.2f")

# Dropdowns for Unit Selection
units = {
    "Length": ["meters", "kilometers", "miles"],
    "Weight": ["grams", "kilograms", "pounds"],
    "Temperature": ["Celsius", "Fahrenheit"],
    "Pressure": ["pascals", "kilopascals", "bar", "psi"],
    "Speed": ["meters per second", "kilometers per hour", "miles per hour"]
}

from_unit = st.selectbox("From:", units[conversion_type])
to_unit = st.selectbox("To:", units[conversion_type])

# 🎯 Convert Button
if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit)
    st.success(f"Converted Value: {result:.2f} {to_unit}")

# 📌 Footer
st.markdown(
    """
    ---
    <p style="text-align: center;">
        👨‍💻 <b>Developed by <span style="color: rgb(12, 83, 237);">Ummay Kulsoom</span></b> | 🚀 Luxury Streamlit Unit Converter
    </p>
    """,
    unsafe_allow_html=True
)
