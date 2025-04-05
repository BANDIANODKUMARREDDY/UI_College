import streamlit as st

# Title
st.title("Takshashila University Fee Calculator (2025-26)")

# Percentage input
percentage = st.number_input("Enter your 12th/HSC Percentage:", min_value=0.0, max_value=100.0, step=0.1)

# Course category
course_category = st.selectbox("Select Programme Type", ["Regular Programmes", "Flagship Programmes"])

# Courses based on category
if course_category == "Regular Programmes":
    courses = {
        "Computer Science Engineering": [107500, 127500, 140000, 150000],
        "Information Technology": [57500, 77500, 90000, 100000],
        "Electronics and Communication Engineering": [57500, 77500, 90000, 100000]
    }
else:
    courses = {
        "CSE (AI & ML) - XEBIA": [121500, 141500, 154000, 164000],
        "CSE (AI & ML) - SUNSTONE": [121500, 141500, 154000, 164000],
        "CSE (Cyber Security) - IBM": [117500, 137500, 150000, 160000],
        "CSE (AI & DS) - IBM": [117500, 137500, 150000, 160000],
        "CSE (Data Engg. & Business Analytics) - TRANSORG": [119500, 139500, 152000, 162000],
        "ECE (IoT) - IBM": [67500, 87500, 100000, 110000]
    }

# Course selection
selected_course = st.selectbox("Select Course", list(courses.keys()))

# Calculate based on percentage
def get_fee(percentage, fee_list):
    if percentage > 90:
        return fee_list[0]
    elif 75 <= percentage <= 90:
        return fee_list[1]
    elif 60 <= percentage < 75:
        return fee_list[2]
    else:
        return fee_list[3]

# Calculate and display fee
if st.button("Calculate Fee"):
    fee = get_fee(percentage, courses[selected_course])
    st.success(f"🎓 Annual Fee for {selected_course}: ₹{fee:,}/Year")

# Hostel fee options
st.subheader("🏨 Hostel Fee Structure (Optional)")
hostel_room = st.selectbox("Choose Room Type", ["None", "4 in 1 (Non-AC)", "3 in 1 (Non-AC)", "2 in 1 (AC)"])
hostel_fees = {
    "None": 0,
    "4 in 1 (Non-AC)": 75000,
    "3 in 1 (Non-AC)": 85000,
    "2 in 1 (AC)": 120000
}

if hostel_room != "None":
    st.info(f"🛏️ Hostel Fee: ₹{hostel_fees[hostel_room]:,}/Year")

    st.success(f"📌 **Total (Tuition + Hostel): ₹{fee + hostel_fees[hostel_room]:,}/Year**")
