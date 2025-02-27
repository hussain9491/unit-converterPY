# create a unit converter with streamlit python

import streamlit as st
import requests  # for currency conversion

# Add custom CSS
st.markdown("""
<style>
    .main {
        padding: 20px;
        border-radius: 10px;
    }
    
    .stSelectbox {
        border-radius: 8px;
    }
    
    .stNumberInput {
        border-radius: 8px;
    }
    
    div.stButton > button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 10px 24px;
        transition: all 0.3s ease-in-out;
    }
    
    div.stButton > button:hover {
        background-color: #45a049;
        transform: translateY(-2px);
    }
    
    .title-container {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        text-align: center;
    }
    
    .result-container {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-top: 20px;
    }
    
    .category-label {
        font-size: 18px;
        font-weight: bold;
        margin-bottom: 10px;
        color: #333;
    }
    
    .unit-label {
        font-size: 16px;
        color: #666;
    }
    
    .check-button {
        background-color: #1e88e5;
        color: white;
        padding: 10px 20px;
        border-radius: 8px;
        border: none;
        cursor: pointer;
        margin: 10px 0;
        width: 100%;
    }
    
    .input-container {
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 8px;
        margin: 10px 0;
    }
    
    .feature-box {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Add sidebar for additional features
with st.sidebar:
    st.markdown("<h3 style='text-align: center;'>Advanced Features</h3>", unsafe_allow_html=True)
    
    # Precision selector
    precision = st.slider("Decimal Precision", 0, 10, 4)
    
    # Unit preferences
    st.markdown("### Default Units")
    default_length = st.selectbox("Default Length Unit", ["Meters", "Feet"])
    default_weight = st.selectbox("Default Weight Unit", ["Kilograms", "Pounds"])
    
    # Theme selection
    theme = st.selectbox("Color Theme", ["Blue", "Green", "Purple"])
    
    # Scientific notation option
    scientific_notation = st.checkbox("Use Scientific Notation")

# Main content
st.markdown("""
<div class="title-container">
    <h1 style='color: #1e88e5;'>Advanced Unit Converter ⚡✅</h1>
</div>
""", unsafe_allow_html=True)

# Create two columns for input
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="input-container">', unsafe_allow_html=True)
    category = st.selectbox(
        "Select Conversion Category",
        ["Length", "Weight", "Temperature", "Angle", "Speed", "Time", 
         "Volume", "Pressure", "Energy", "Power", "Data Transfer Rate"]
    )
    input_value = st.number_input("Enter value to convert", value=0.0)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="input-container">', unsafe_allow_html=True)
    # Unit selection based on category
    if category == "Length":
        units = ["Meters", "Kilometers", "Miles", "Feet", "Inches", "Yards", "Centimeters", "Millimeters"]
    elif category == "Weight":
        units = ["Kilograms", "Grams", "Pounds", "Ounces"]
    elif category == "Temperature":
        units = ["Celsius", "Fahrenheit", "Kelvin"]
    elif category == "Angle":
        units = ["Degrees", "Radians", "Gradians"]
    elif category == "Speed":
        units = ["Meters per second", "Kilometers per hour", "Miles per hour", "Knots"]
    elif category == "Time":
        units = ["Seconds", "Minutes", "Hours", "Days", "Weeks", "Months", "Years"]
    elif category == "Volume":
        units = ["Liters", "Milliliters", "Cubic meters", "Gallons (US)", "Cubic feet"]
    elif category == "Pressure":
        units = ["Pascal", "Bar", "PSI", "Atmosphere", "Kilopascal"]
    elif category == "Energy":
        units = ["Joules", "Calories", "Kilowatt hours", "Electron volts", "BTU"]
    elif category == "Power":
        units = ["Watts", "Kilowatts", "Horsepower", "BTU/hour"]
    elif category == "Data Transfer Rate":
        units = ["Bits per second", "Kilobits per second", "Megabits per second", 
                  "Gigabits per second", "Bytes per second", "Kilobytes per second",
                  "Megabytes per second", "Gigabytes per second"]
    
    from_unit = st.selectbox("From:", units, index=units.index(default_length) if category == "Length" else 0)
    to_unit = st.selectbox("To:", units, index=0)
    st.markdown('</div>', unsafe_allow_html=True)

# Add check button
if st.button("Convert", key="convert_button"):
    # Initialize conversion history if it doesn't exist
    if 'conversion_history' not in st.session_state:
        st.session_state.conversion_history = []
    
    # Perform conversion (your existing conversion logic)
    if category == "Length":
        # Length conversion
        length_factors = {
            "Meters": 1,
            "Kilometers": 1000,
            "Miles": 1609.34,
            "Feet": 0.3048,
            "Inches": 0.0254
        }
        result = input_value * length_factors[from_unit] / length_factors[to_unit]
    elif category == "Weight":
        # Weight conversion
        weight_factors = {
            "Kilograms": 1,
            "Grams": 0.001,
            "Pounds": 0.453592,
            "Ounces": 0.0283495
        }
        result = input_value * weight_factors[from_unit] / weight_factors[to_unit]
    elif category == "Temperature":
        # Temperature conversion
        if from_unit == to_unit:
            result = input_value
        else:
            # Convert to Celsius first
            if from_unit == "Fahrenheit":
                celsius = (input_value - 32) * 5/9
            elif from_unit == "Kelvin":
                celsius = input_value - 273.15
            else:
                celsius = input_value
            
            # Convert from Celsius to target unit
            if to_unit == "Fahrenheit":
                result = (celsius * 9/5) + 32
            elif to_unit == "Kelvin":
                result = celsius + 273.15
            else:
                result = celsius
    elif category == "Angle":
        angle_factors = {
            "Degrees": 1,
            "Radians": 57.2958,
            "Gradians": 0.9
        }
        result = input_value * angle_factors[to_unit] / angle_factors[from_unit]
    elif category == "Speed":
        speed_factors = {
            "Meters per second": 1,
            "Kilometers per hour": 0.277778,
            "Miles per hour": 0.44704,
            "Knots": 0.514444
        }
        result = input_value * speed_factors[from_unit] / speed_factors[to_unit]
    elif category == "Time":
        time_factors = {
            "Seconds": 1,
            "Minutes": 60,
            "Hours": 3600,
            "Days": 86400,
            "Weeks": 604800,
            "Months": 2592000,  # Approximate (30 days)
            "Years": 31536000   # Non-leap year
        }
        result = input_value * time_factors[from_unit] / time_factors[to_unit]
    elif category == "Volume":
        volume_factors = {
            "Liters": 1,
            "Milliliters": 0.001,
            "Cubic meters": 1000,
            "Gallons (US)": 3.78541,
            "Cubic feet": 28.3168
        }
        result = input_value * volume_factors[from_unit] / volume_factors[to_unit]
    elif category == "Pressure":
        pressure_factors = {
            "Pascal": 1,
            "Bar": 100000,
            "PSI": 6894.76,
            "Atmosphere": 101325,
            "Kilopascal": 1000
        }
        result = input_value * pressure_factors[from_unit] / pressure_factors[to_unit]
    elif category == "Energy":
        energy_factors = {
            "Joules": 1,
            "Calories": 4.184,
            "Kilowatt hours": 3600000,
            "Electron volts": 1.602176634e-19,
            "BTU": 1055.06
        }
        result = input_value * energy_factors[from_unit] / energy_factors[to_unit]
    elif category == "Power":
        power_factors = {
            "Watts": 1,
            "Kilowatts": 1000,
            "Horsepower": 745.7,
            "BTU/hour": 0.29307107
        }
        result = input_value * power_factors[from_unit] / power_factors[to_unit]
    elif category == "Data Transfer Rate":
        data_factors = {
            "Bits per second": 1,
            "Kilobits per second": 1000,
            "Megabits per second": 1000000,
            "Gigabits per second": 1000000000,
            "Bytes per second": 8,
            "Kilobytes per second": 8000,
            "Megabytes per second": 8000000,
            "Gigabytes per second": 8000000000
        }
        result = input_value * data_factors[from_unit] / data_factors[to_unit]

    # Format result based on settings
    if scientific_notation and abs(result) < 0.0001:
        result_text = f"{result:.{precision}e}"
    else:
        result_text = f"{result:.{precision}f}"
    
    # After calculating the result, update the history
    new_conversion = {
        'from_value': float(input_value),
        'from_unit': str(from_unit),
        'to_value': float(result),
        'to_unit': str(to_unit),
        'category': str(category)
    }
    
    # Add new conversion to history
    st.session_state.conversion_history.insert(0, new_conversion)
    # Keep only last 5 conversions
    st.session_state.conversion_history = st.session_state.conversion_history[:5]
    
    # Display result with new styling
    st.markdown(f"""
    <div class="result-container">
        <h3 style='text-align: center; color: #1e88e5;'>Result ✅</h3>
        <div style='text-align: center; color: #808080; font-size: 24px; padding: 10px; background-color: #f8f9fa; border-radius: 8px;'>
            {input_value:.{precision}f} {from_unit} = {result_text} {to_unit}
        </div>
    </div>
    """, unsafe_allow_html=True)

# Show conversion history (move outside the button click)
st.markdown("<h3 style='margin-top: 30px;'>Recent Conversions</h3>", unsafe_allow_html=True)
if 'conversion_history' in st.session_state and st.session_state.conversion_history:
    for conv in st.session_state.conversion_history:
        st.markdown(f"""
        <div class="feature-box">
            <span style="color: #1e88e5;">{conv['category']}</span>: 
            {conv['from_value']:.{precision}f} {conv['from_unit']} ➜ 
            {conv['to_value']:.{precision}f} {conv['to_unit']}
        </div>
        """, unsafe_allow_html=True)
else:
    st.markdown("""
    <div class="feature-box" style="text-align: center; color: #666;">
        No conversion history yet
    </div>
    """, unsafe_allow_html=True)

