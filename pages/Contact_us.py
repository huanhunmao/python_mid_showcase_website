import streamlit as st
import send_email as sd

st.header('Contact us')

with st.form(key="email_forms"):
    user_email = st.text_input('Your Email')
    message = st.text_area('Your Message')
    button = st.form_submit_button('Submit')

    print(button)
    if button:
        # message = message + user_email
        sd.send_email(user_email, message)