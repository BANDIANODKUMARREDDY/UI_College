import streamlit as st

# Styling
st.markdown("""
    <style>
        .title {
            text-align: center;
            font-size: 32px;
            font-weight: bold;
            color: #003366;
        }
        .subtitle {
            text-align: center;
            font-size: 18px;
            color: #555;
            font-weight: bold;
        }
        .fee-box {
            padding: 15px;
            border-radius: 10px;
            background-color: #f5faff;
            text-align: center;
            font-size: 20px;
            color: #004d00;
            font-weight: bold;
        }
        .footer {
            font-size: 14px;
            color: gray;
            margin-top: 30px;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 class="title">🏫 SAI University - Fee Structure (2025)</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="subtitle">Per Annum Fee with Scholarship Options</h2>', unsafe_allow_html=True)

# Fee data
fee_data = {
    "School of Computing and Data Science": {
        "B.Tech - Computer Science": 400000,
        "B.Tech - Computer Science with AI": 400000,
        "B.Tech - Computer Science with Data Science": 400000,
        "B.Tech - Data Science": 400000
    },
    "School of Artificial Intelligence": {
        "B.Tech - Artificial Intelligence": 500000
    },
    "School of Technology": {
        "B.Tech - Bio Technology": 400000,
        "B.Tech - Environmental Engineering & Sustainability": 400000
    }
}

# Scholarship logic
def calculate_scholarship_fee(school, fee, percentage):
    if school == "School of Artificial Intelligence":
        if percentage > 80:
            return 360000
        elif 70 <= percentage <= 80:
            return 375000
    else:  # Other schools
        if percentage > 80:
            return 250000
        elif 70 <= percentage <= 80:
            return 300000
    return fee  # No scholarship

# Dropdowns
selected_school = st.selectbox("Select School", list(fee_data.keys()))
selected_program = st.selectbox("Select Program", list(fee_data[selected_school].keys()))
original_fee = fee_data[selected_school][selected_program]

# Text input for percentage
percentage_input = st.text_input("Enter your Intermediate (HSC) %", placeholder="Example: 78.5")

# Validate and show fee
if percentage_input:
    try:
        percentage = float(percentage_input)
        if 0 <= percentage <= 100:
            final_fee = calculate_scholarship_fee(selected_school, original_fee, percentage)
            st.markdown(f'<div class="fee-box">🎓 Tuition Fee for {selected_program}: ₹{final_fee:,} per annum</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="footer">Scholarship based on entered percentage ({percentage}%) | Original Fee: ₹{original_fee:,}</div>', unsafe_allow_html=True)
        else:
            st.error("Please enter a valid percentage between 0 and 100.")
    except ValueError:
        st.error("Please enter a numeric value for percentage.")
