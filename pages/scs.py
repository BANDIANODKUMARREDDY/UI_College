import streamlit as st

st.title("SCSVMV - Kanchi University Fee Calculator")
st.subheader("Fee Structure 2025-26")

program_type = st.selectbox("Select Program Type", [
    "CSE & AI-related Programs",
    "ECE & Robotics-related Programs",
    "Mechanical, Mechatronics, Civil, EIE",
    "Lateral Entry (CSE, ECE, IT)",
    "Lateral Entry (EEE, MECH, CIVIL, EIE)",
    "BBA",
    "MBA",
    "MCA"
])

percentage = None
if "Lateral Entry" in program_type or "Programs" in program_type:
    percentage = st.number_input("Enter PCM Percentage", min_value=0.0, max_value=100.0, step=0.1)

# Tuition Fee Logic
fee = None
if program_type == "CSE & AI-related Programs":
    if percentage >= 90:
        fee = 100000
    elif 75 <= percentage < 90:
        fee = 130000
    elif 60 <= percentage < 75:
        fee = 150000
    else:
        fee = 190000

elif program_type == "ECE & Robotics-related Programs":
    if percentage >= 90:
        fee = 100000
    elif 75 <= percentage < 90:
        fee = 110000
    elif 60 <= percentage < 75:
        fee = 120000
    else:
        fee = 170000

elif program_type == "Mechanical, Mechatronics, Civil, EIE":
    if percentage >= 60:
        fee = 60000
    else:
        fee = 120000

elif program_type == "Lateral Entry (CSE, ECE, IT)":
    if percentage > 70:
        fee = 80000
    elif 50 <= percentage <= 70:
        fee = 120000

elif program_type == "Lateral Entry (EEE, MECH, CIVIL, EIE)":
    if percentage > 70:
        fee = 60000
    elif 50 <= percentage <= 70:
        fee = 120000

elif program_type == "BBA":
    fee = 50000
elif program_type == "MBA":
    fee = 125000
elif program_type == "MCA":
    fee = 61000

# Display Fee
if fee is not None:
    st.success(f"Tuition Fee per Year: ₹{fee:,}")

# Optional Add-ons
st.markdown("---")
st.markdown("**Other Fees (First Year Only)**")
st.markdown("- Admission, Lab, Career Dev Fee: ₹25,000")
st.markdown("- Hostel Fee: ₹85,000")
