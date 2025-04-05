import streamlit as st

st.set_page_config(page_title="College Portal Access", layout="wide")
st.title("🎓 College Portal Access")

# College name and matching file name in 'pages/' folder
colleges = [
    ("Akash", "akash"),
    ("Amritha", "Amritha"),
    ("Hindustan", "Hindustan"),
    ("IES", "IES"),
    ("IZEE", "IZEE"),
    ("NIMS", "NIMS"),
    ("Sathyabama", "Sathyabama"),
    ("Saveetha", "saveetha"),
    ("SRM", "SRM"),
    ("SRMC", "SRMC"),
    ("Veltech", "Veltech"),
    ("Bharath", "bharath"),
    ("SAII", "SAII"),
    ("SAI", "sai"),
    ("Thanksha", "thanksha"),
    ("SCS", "scs")
]

# Display buttons in rows of 3
cols = st.columns(3)

for index, (label, filename) in enumerate(colleges):
    with cols[index % 3]:
        if st.button(label):
            st.switch_page(f"pages/{filename}.py")
