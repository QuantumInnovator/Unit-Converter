import streamlit as st
st.markdown(
    """
<style>
    body {
        background-color:rgb(57, 57, 75);
        color : white;
    }
    .stApp {
        background : linear-gradient(135deg, #bcbcbc, #cfe2f3);
        padding: 30px;
        border-radius : 15px; 
        box-shadow: 0px 10px rgba(0, 0, 0, 0.3);
    }
    h1{
        text-align: center;
        font-size: 36px;
        color : white;
    }
    .stButton>button{
        background-color: linear-gradient(135deg, #bcbcbc,rgb(209, 23, 163)) ;
        color : white;
        font-size: 18px;
        border-radius: 10px;
        transition:  0.3s;
        padding: 10px 20px;
        border-radius: 10px;
        box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.4);
    }
    .stButton>button:hover{
        background: linear-gradient(45deg, #92fe9d, #00c9ff);
        transform: scale(1.05);
    }
    .result-box{
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        background: rgba(255, 255, 255, 0.1);
        padding: 25px;
        border-radius: 15px;
        margin-top: 20px;
        box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.4);
    }
    .footer{
        text-align: center;
        margin-top: 20px;
        font-size: 14px;
        color: #666;
    }
</style>
""",
    unsafe_allow_html=True
)
#titles
st.markdown("<h1>🔄 Unit Converter using Python and Streamlit 🔄</h1>", unsafe_allow_html=True)
st.write("Easily convert between different units of length ✈️, weight 💪, temperature 🌡️")

#sidebar menu
conversion_type = st.sidebar.selectbox("Select Conversion Type", ["📊 Length", "💪 Weight", "🌡️ Temperature"])
value = st.number_input("Enter the value to convert", value=0.0, min_value=0.0, step=0.1)
col1 , col2 = st.columns(2) 

if conversion_type == "📊 Length":
    with col1:
        from_unit = st.selectbox("From Unit", ["Meters", "Kilograms", "Feet", "Miles","Yards","Inches","Centimeters","Millimeters"])
    with col2:
        to_unit = st.selectbox("To Unit", ["Meters", "Kilograms", "Feet", "Miles","Yards","Inches","Centimeters","Millimeters"])

elif conversion_type == "💪 Weight":
    with col1:
        from_unit = st.selectbox("From Unit", ["Kilograms", "Grams", "Pounds", "Ounces","Milligrams"])
    with col2:
        to_unit = st.selectbox("To Unit", ["Kilograms", "Grams", "Pounds", "Ounces","Milligrams"])

elif conversion_type == "🌡️ Temperature":
    with col1:
        from_unit = st.selectbox("From Unit", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To Unit", ["Celsius", "Fahrenheit", "Kelvin"])

#Converted Function

def length_conversion(value, from_unit, to_unit):
    length_units = {
        "Meters": 1.0,
        "Kilometers": 0.001,
        "Centimeters": 100.0,
        "Millimeters": 1000.0,
        "Feet": 3.28084,
        "Miles": 0.000621371,
        "Yards": 1.09361,
        "Inches": 39.3701,
    }
    return (value / length_units[from_unit] * length_units[to_unit])

def weight_converter(value, from_unit, to_unit):
    weight_units = {
        "Kilograms": 1.0,
        "Grams": 1000.0,
        "Pounds": 2.20462,
        "Ounces": 35.274,
        "Milligrams": 1000000.0,    
    }
    return (value / weight_units[from_unit] * weight_units[to_unit] )

def temperature_converter(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32 if to_unit == "Fahrenheit" else value + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32 if to_unit == "Fahrenheit" else value
    else:
        return value
    

#Button for conversion
if st.button("🔄 Convert"):
    if conversion_type == "📊 Length":
        result = length_conversion(value, from_unit, to_unit)
    elif conversion_type == "💪 Weight":
        result = weight_converter(value, from_unit, to_unit)
    elif conversion_type == "🌡️ Temperature":
        result = temperature_converter(value, from_unit, to_unit)   

    st.markdown(f"<div class='result-box'>✅ {value} {from_unit} is equal to {result:.4f} {to_unit}</div>", unsafe_allow_html=True)  

    st.markdown(f"<div class='footer'>👨‍💻 Developed by Raffay 🚀</div>", unsafe_allow_html=True)    
    

