import streamlit as st

# IES University Fee Structure Data (Extracted from Image)
fee_structure = {
    "1st SEM (including hostel)": "₹1,73,500.00",
    "2nd semester": "₹36,000.00",
    "3rd semester": "₹68,500.00",
    "4th semester": "₹68,500.00",
    "5th semester": "₹68,500.00",
    "6th semester": "₹68,500.00",
    "7th semester": "₹68,500.00",
    "8th semester": "₹68,500.00",
    "TOTAL PACKAGE (4 YEARS INCLUDING HOSTEL, FOOD & ACCOMMODATION)": "6.28 LAKHS"
}

# Custom Styling for Enhanced UI
st.markdown(
    """
    <style>
        .title {
            text-align: center;
            font-size: 32px;
            color: #B22222;
            font-weight: bold;
        }
        .subtitle {
            text-align: center;
            font-size: 20px;
            color: #333;
            font-weight: bold;
        }
        .dropdown {
            text-align: center;
            font-size: 18px;
            font-weight: bold;
        }
        .fee-box {
            padding: 15px;
            border-radius: 10px;
            background-color: #f4f4f4;
            text-align: center;
            font-size: 22px;
            color: #2E8B57;
            font-weight: bold;
        }
        .disclaimer {
            text-align: center;
            margin-top: 20px;
            font-size: 14px;
            color: gray;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Display University Name & Title
st.markdown('<h1 class="title">🏫 IES University - Fee Structure (2025-26)</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="subtitle">B.Tech Program - Semester-wise Fees</h2>', unsafe_allow_html=True)

# Dropdown for semester selection
semesters = list(fee_structure.keys())[:-1]  # Exclude total from dropdown
selected_semester = st.selectbox("Select a Semester", semesters)

# Display the selected semester fee
st.markdown(f'<div class="fee-box">💰 Fee for {selected_semester}: {fee_structure[selected_semester]}</div>', unsafe_allow_html=True)

# Display total package info
st.markdown('<h2 class="subtitle" style="margin-top: 30px;">📦 Total Package</h2>', unsafe_allow_html=True)
st.markdown(f'<div class="fee-box">💼 {list(fee_structure.keys())[-1]}: ₹{fee_structure["TOTAL PACKAGE (4 YEARS INCLUDING HOSTEL, FOOD & ACCOMMODATION)"]}</div>', unsafe_allow_html=True)

# Disclaimer
st.markdown('<div class="disclaimer">Disclaimer: Including hostel and accommodation</div>', unsafe_allow_html=True)
