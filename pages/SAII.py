import streamlit as st

st.title("SAII University Fee Calculator")
st.subheader("School of Engineering & Technology - UG (4 Years)")

programs = {
    "B.Tech. - Artificial Intelligence and Data Science": "tiered",
    "B.Tech. - Artificial Intelligence and Machine Learning": "tiered",
    "B.Tech. - Computer Science and Engineering": "tiered",
    "B.Tech. - Computer Science and Engineering (Cyber Security)": "tiered",
    "B.Tech. - Information Technology": "tiered",
    "B.Tech. - Agriculture Engineering": "flat",
    "B.Tech. - Biomedical Engineering": "flat",
    "B.Tech. - Biotechnology": "flat",
    "Computer Science and Engineering (IoT)": "flat",
    "B.Tech. - Electronics and Communication Engineering": "flat",
    "B.Tech. - Electrical and Electronics Engineering": "flat",
    "B.Tech. - Mechanical Engineering": "flat"
}

selected_program = st.selectbox("Select Program", list(programs.keys()))

fee = None
if programs[selected_program] == "tiered":
    percentage = st.number_input("Enter HSC Percentage", min_value=0.0, max_value=100.0, step=0.1)
    if percentage >= 70:
        fee = 75000
    elif 60 <= percentage < 70:
        fee = 87500
    elif 50 <= percentage < 60:
        fee = 100000
    else:
        fee = 112500
else:
    fee = 50000

if fee:
    st.success(f"Tuition Fee per Semester: ₹{fee:,}")
