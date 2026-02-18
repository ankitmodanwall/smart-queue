import streamlit as st

st.set_page_config(page_title="AI Smart Queue", layout="centered")

st.title("AI Smart Queue System for Hospitals")

# Initialize queue
if "queue" not in st.session_state:
    st.session_state.queue = []

# Sidebar doctor settings
st.sidebar.header("Doctor Settings")
doctor_count = st.sidebar.slider("Available Doctors", 1, 5, 1)
avg_consult_time = st.sidebar.slider("Avg Consultation Time (mins)", 5, 30, 10)

# Patient registration
st.header("Patient Registration")

name = st.text_input("Patient Name")
urgency = st.selectbox("Urgency Level", ["Low", "Medium", "High"])

if st.button("Add to Queue"):
    if name:
        st.session_state.queue.append({
            "name": name,
            "urgency": urgency
        })
        st.success(f"{name} added to queue")
    else:
        st.warning("Please enter patient name")

# Priority logic
priority_order = {"High": 1, "Medium": 2, "Low": 3}

sorted_queue = sorted(
    st.session_state.queue,
    key=lambda x: priority_order[x["urgency"]]
)

# Queue display
st.header("Smart Queue")

if len(sorted_queue) == 0:
    st.info("No patients in queue")
else:
    effective_time = avg_consult_time / doctor_count

    for i, patient in enumerate(sorted_queue):
        wait_time = int(i * effective_time)

        st.write(
            f"Token {i+1} | {patient['name']} | "
            f"Urgency: {patient['urgency']} | "
            f"Estimated Wait: {wait_time} mins"
        )

# Clear queue button
st.markdown("---")
if st.button("Clear Queue"):
    st.session_state.queue = []
    st.success("Queue cleared")

