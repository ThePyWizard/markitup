import streamlit as st
from auth import sign_in, sign_up
from attendance import attendance_form, view_attendance

def main():
    st.title("Class Attendance Tracker")

    menu = ["Home", "Login", "SignUp"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
    elif choice == "Login":
        st.subheader("Login Section")

        email = st.text_input("Email")
        password = st.text_input("Password", type='password')
        if st.button("Login"):
            user = sign_in(email, password)
            if user:
                st.success(f"Welcome {email}")
                st.session_state['user'] = user
            else:
                st.error("Invalid email or password")

    elif choice == "SignUp":
        st.subheader("Create New Account")

        email = st.text_input("Email")
        password = st.text_input("Password", type='password')
        if st.button("Sign Up"):
            user = sign_up(email, password)
            if user:
                st.success("Account created successfully")
            else:
                st.error("Failed to create account")

    if 'user' in st.session_state:
        user_id = st.session_state['user']['localId']
        attendance_form(user_id)
        view_attendance(user_id)

if __name__ == '__main__':
    main()
