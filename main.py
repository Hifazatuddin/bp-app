import streamlit as st

st.title("❤🎂Hello, Azalaan!🧨")
st.markdown("This app is prepare for NAughty Boy.")
# ak birday app banana ha 
user_input = st.text_input("Enter your name:")
if user_input:
    """"🎉 Happy Birthday! 🎉

Wishing you a wonderful birthday filled with joy, success, and memorable moments. \n May the year ahead bring you new achievements, personal growth, and opportunities to fulfill your aspirations. You truly deserve all the best today and in the future.

"""
    st.write(f"Have a fantastic and rewarding year ahead! 🌟 , {user_input}!")   
    print(f"Wellcom to A New Journay ",user_input)  # This will print to the console, not the app

