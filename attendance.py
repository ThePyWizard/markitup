import streamlit as st
from utils.firebase_utils import add_attendance, get_attendance

def attendance_form(user_id):
    st.subheader("Fill Attendance Form")
    date = st.date_input("Date")
    time = st.time_input("Time")
    event_details = st.text_area("Event Details")
    if st.button("Submit"):
        add_attendance(user_id, date, time, event_details)
        st.success("Attendance added successfully")

def view_attendance(user_id):
    st.subheader("Your Attendance")
    attendance = get_attendance(user_id)
    for record in attendance:
        st.write(record)
