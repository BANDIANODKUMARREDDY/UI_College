import streamlit as st

st.title("Bharath Institute B.Tech Fee Calculator")
st.subheader("Applicable for Andhra Pradesh and Telangana (2024-2025)")

# Define program categories
tiered_programs = {
    "CSE": [("90% Above", 125000), ("70% - 89.9%", 150000), ("60% - 69.9%", 175000),
            ("50% - 59.9%", 200000), ("Below 50%", 225000)],
    "CSE with AI / AIML / Cyber Security / Data Science / IoT / AIML (IOA UK) / AI & DS (UPGRAD)":
        [("90% Above", 150000), ("70% - 89.9%", 175000), ("60% - 69.9%", 200000),
         ("50% - 59.9%", 225000), ("Below 50%", 250000)],
    "CSE (In Association with IBM)": [("Any PCM %", 250000)]
}

flat_fee_programs = {
    "Electronics & Communication Engineering": 100000,
    "Information Technology": 150000,
    "Aeronautical Engineering": 100000,
    "Aerospace Engineering": 100000,
    "Industrial Biotechnology": 100000,
    "Biotech - Agricultural Specialization": 100000,
    "Biomedical Engineering": 100000,
    "Biotech - Genetic Engineering Specialization": 100000,
    "Mechanical Engineering": 75000,
    "Mechatronics Engineering": 75000,
    "Electrical & Electronics Engineering": 75000,
    "Civil Engineering": 75000,
    "Automobile Engineering": 75000,
    "B.Arch": 125000
}

# Combine programs into a single dropdown
all_programs = list(tiered_programs.keys()) + list(flat_fee_programs.keys())
selected_program = st.selectbox("Select Program", all_programs)

fee = None

if selected_program in tiered_programs:
    if selected_program == "CSE (In Association with IBM)":
        fee = tiered_programs[selected_program][0][1]
    else:
        percentage = st.number_input("Enter PCM Percentage", min_value=0.0, max_value=100.0, step=0.1)
        if percentage >= 90:
            fee = tiered_programs[selected_program][0][1]
        elif 70 <= percentage < 90:
            fee = tiered_programs[selected_program][1][1]
        elif 60 <= percentage < 70:
            fee = tiered_programs[selected_program][2][1]
        elif 50 <= percentage < 60:
            fee = tiered_programs[selected_program][3][1]
        else:
            fee = tiered_programs[selected_program][4][1]
else:
    fee = flat_fee_programs[selected_program]

if fee:
    st.success(f"Tuition Fee per Year: ₹{fee:,}")
